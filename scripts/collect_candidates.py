#!/usr/bin/env python3
"""Collect recent DOI metadata and build a history-aware candidate manifest."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


JOURNALS = {
    "AER": "0002-8282",
    "JPE": "0022-3808",
    "QJE": "0033-5533",
    "JET": "0022-0531",
    "IIO": "0167-7187",
    "RAND J": "0741-6261",
    "Econometrica": "0012-9682",
    "ReStud": "0034-6527",
}

TOPIC_PATTERNS = {
    "io": r"compet|collu|pricing|price discrimination|merger|acquisition|market power|markup|entry|auction|antitrust|oligopol|monopol|vertical|search|advertis",
    "platform": r"platform|two-sided|recommend|ranking|algorithm|artificial intelligence|privacy|data|digital|intermediar",
    "supply_chain": r"supply chain|procurement|contract|bargain|production network|firm-to-firm|global value chain|sourcing|supplier|buyer|resilien|disruption",
    "theory": r"equilibrium|mechanism design|information design|persuasion|game|screening|matching|contract theory",
    "environment": r"environment|climate|pollut|emission|carbon|decarbon|renewable|clean energy|energy transition|green innov|conservation|biodiversity|deforestation|cap.and.trade|fossil|electricity|adaptation|resource extraction|water scarcity",
}


def normalize_doi(value: str | None) -> str:
    value = (value or "").strip().lower()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value)


def normalize_title(value: str | None) -> str:
    value = re.sub(r"（(?:环境|已下载)）", "", html.unescape(value or ""))
    value = unicodedata.normalize("NFKD", value).casefold()
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^\w\s]", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip()


def strip_tags(value: str | None) -> str:
    text = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def date_parts(item: dict, key: str) -> str | None:
    parts = item.get(key, {}).get("date-parts", [[]])[0]
    if not parts:
        return None
    vals = list(parts) + [1, 1]
    try:
        return dt.date(int(vals[0]), int(vals[1]), int(vals[2])).isoformat()
    except (TypeError, ValueError):
        return None


def request_json(url: str, attempts: int = 4, timeout: int = 25) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "economic-journal-io-radar/1.0 (academic literature monitoring)",
            "Accept": "application/json",
        },
    )
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt)
        except urllib.error.URLError:
            if attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def parse_history(history_dir: Path) -> tuple[set[str], set[str], list[str]]:
    dois: set[str] = set()
    titles: set[str] = set()
    files = sorted(history_dir.glob("经济学顶刊速览-*.md"))
    bold_entry = re.compile(r"^\*\*\d+\.\s+.*?\((?:19|20)\d{2}(?:-\d{2}){0,2}\)\.\s+(.+?)\.\s+(?:AER|JPE|QJE|JET|IIO|RAND J|Econometrica|ReStud)[,\.]", re.M)
    list_entry = re.compile(r"^\d+\.\s+.*?\((?:19|20)\d{2}(?:-\d{2}){0,2}\)\.\s+(.+?)\.\s+(?:AER|JPE|QJE|JET|IIO|RAND J|Econometrica|ReStud)\b", re.M)
    doi_re = re.compile(r"(?:https?://doi\.org/|\bdoi:\s*)(10\.\d{4,9}/[-._;()/:a-z0-9]+)", re.I)
    for path in files:
        text = path.read_text(encoding="utf-8").replace("**", "")
        for match in doi_re.finditer(text):
            dois.add(normalize_doi(match.group(1).rstrip(".,;)")))
        for pattern in (bold_entry, list_entry):
            for match in pattern.finditer(text):
                title = normalize_title(match.group(1))
                if title:
                    titles.add(title)
    return dois, titles, [str(p) for p in files]


def crossref_items(issn: str, since: dt.date) -> list[dict]:
    # Separate filters are a union, not an intersection: old deposits may go online now.
    found: dict[str, dict] = {}
    for date_filter in ("from-created-date", "from-online-pub-date"):
        cursor = "*"
        while True:
            params = urllib.parse.urlencode({
                "filter": f"{date_filter}:{since.isoformat()},type:journal-article",
                "rows": 100, "cursor": cursor,
                "select": "DOI,title,author,abstract,URL,published-online,published-print,issued,created,volume,issue,page,type,publisher,container-title",
            })
            message = request_json(f"https://api.crossref.org/journals/{issn}/works?{params}")["message"]
            items = message["items"]
            for item in items:
                found[normalize_doi(item.get("DOI"))] = item
            next_cursor = message.get("next-cursor")
            if len(items) < 100 or not next_cursor or next_cursor == cursor:
                break
            cursor = next_cursor
    return list(found.values())


def openalex_items(issn: str, since: dt.date) -> list[dict]:
    params = urllib.parse.urlencode(
        {
            "filter": f"primary_location.source.issn:{issn},from_publication_date:{since.isoformat()}",
            "sort": "publication_date:desc",
            "per-page": 200,
            "select": "id,doi,title,publication_date,biblio,primary_location,type",
        }
    )
    # OpenAlex is only a cross-check. Keep its failure budget small so that an
    # optional endpoint cannot stall a weekly run across all seven journals.
    return request_json(
        f"https://api.openalex.org/works?{params}", attempts=2, timeout=15
    )["results"]


def author_name(author: dict) -> str:
    parts = [author.get("given", "").strip(), author.get("family", "").strip()]
    return " ".join(part for part in parts if part)


def topical_hits(title: str, abstract: str) -> dict[str, list[str]]:
    haystack = f"{title} {abstract}".casefold()
    result = {}
    for category, pattern in TOPIC_PATTERNS.items():
        hits = sorted({m.group(0).casefold() for m in re.finditer(pattern, haystack, re.I)})
        if hits:
            result[category] = hits
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--history-dir", type=Path, required=True)
    parser.add_argument("--lookback", type=int, default=45)
    parser.add_argument("--as-of", default=dt.date.today().isoformat())
    parser.add_argument("--openalex", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    as_of = dt.date.fromisoformat(args.as_of)
    since = as_of - dt.timedelta(days=args.lookback)
    history_dois, history_titles, history_files = parse_history(args.history_dir)
    manifest = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "as_of": as_of.isoformat(),
        "since": since.isoformat(),
        "lookback_days": args.lookback,
        "history": {
            "files": history_files,
            "doi_count": len(history_dois),
            "title_count": len(history_titles),
        },
        "journals": {},
        "candidates": [],
    }

    seen_manifest_dois: set[str] = set()
    for journal, issn in JOURNALS.items():
        report = {"issn": issn, "crossref_count": 0, "openalex_count": None, "errors": []}
        try:
            items = crossref_items(issn, since)
            report["crossref_count"] = len(items)
        except Exception as exc:  # network failures must be visible in the manifest
            items = []
            report["errors"].append(f"Crossref: {type(exc).__name__}: {exc}")

        openalex_dois: set[str] = set()
        if args.openalex:
            try:
                oa_items = openalex_items(issn, since)
                report["openalex_count"] = len(oa_items)
                openalex_dois = {normalize_doi(x.get("doi")) for x in oa_items if normalize_doi(x.get("doi"))}
            except Exception as exc:
                report["errors"].append(f"OpenAlex: {type(exc).__name__}: {exc}")

        crossref_dois: set[str] = set()
        for item in items:
            title = (item.get("title") or [""])[0].strip()
            doi = normalize_doi(item.get("DOI"))
            if not title or not doi or doi in seen_manifest_dois:
                continue
            if re.search(r"^(front matter|back matter|backmatter|issue information|recent referees|correction to:)", title, re.I):
                continue
            seen_manifest_dois.add(doi)
            crossref_dois.add(doi)
            normalized_title = normalize_title(title)
            abstract = strip_tags(item.get("abstract"))
            online = date_parts(item, "published-online")
            printed = date_parts(item, "published-print")
            issued = date_parts(item, "issued")
            created = date_parts(item, "created")
            published = online or printed or issued or created
            authors = [author_name(a) for a in item.get("author", []) if author_name(a)]
            seen_by = []
            if doi in history_dois:
                seen_by.append("doi")
            if normalized_title in history_titles:
                seen_by.append("title")
            manifest["candidates"].append(
                {
                    "journal": journal,
                    "issn": issn,
                    "doi": doi,
                    "title": title,
                    "normalized_title": normalized_title,
                    "authors": authors,
                    "first_author": authors[0] if authors else None,
                    "published_date": published,
                    "date_sources": {"online": online, "print": printed, "issued": issued, "created": created},
                    "volume": item.get("volume"),
                    "issue": item.get("issue"),
                    "page": item.get("page"),
                    "status_hint": "issue-assigned" if item.get("volume") or item.get("issue") else "online-first",
                    "publisher_url": item.get("URL") or f"https://doi.org/{doi}",
                    "abstract": abstract or None,
                    "topic_hints": topical_hits(title, abstract),
                    "historical_duplicate": bool(seen_by),
                    "historical_match_by": seen_by,
                }
            )

        if args.openalex and report["openalex_count"] is not None:
            report["crossref_only_dois"] = sorted(crossref_dois - openalex_dois)
            report["openalex_only_dois"] = sorted(openalex_dois - crossref_dois)
        manifest["journals"][journal] = report
        time.sleep(0.35)

    manifest["candidates"].sort(key=lambda x: (x["journal"], x["published_date"] or "", x["title"]), reverse=True)
    manifest["summary"] = {
        "candidate_count": len(manifest["candidates"]),
        "historical_duplicate_count": sum(1 for x in manifest["candidates"] if x["historical_duplicate"]),
        "new_candidate_count": sum(1 for x in manifest["candidates"] if not x["historical_duplicate"]),
    }
    payload = json.dumps(manifest, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
