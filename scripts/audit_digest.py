#!/usr/bin/env python3
"""Validate structural and deduplication invariants of a finished radar digest."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from score_paper import score_paper


JOURNALS = ["AER", "JPE", "QJE", "JET", "IIO", "RAND", "Econometrica", "ReStud", "NBER"]


def normalize_doi(value: str) -> str:
    value = value.strip().lower()
    return re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", value).rstrip(".,;)")


def normalize_title(value: str) -> str:
    value = value.casefold()
    value = re.sub(r"[^\w\s]", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip()


def cjk_count(value: str) -> int:
    return len(re.findall(r"[\u3400-\u9fff]", value))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    text = args.path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []
    scoring_v2 = bool(re.search(r"评分口径[^\n]*v2", text))

    required_sections = ["## 2星观察区", "## 覆盖审计", "## 已收录清单（累计）"]
    for section in required_sections:
        if section not in text:
            errors.append(f"missing required section: {section}")

    audit = text.split("## 覆盖审计", 1)[1] if "## 覆盖审计" in text else ""
    for journal in JOURNALS:
        # Archived reports may predate these added discovery channels.
        if not scoring_v2 and journal in ("ReStud", "NBER") and journal not in text:
            continue
        if journal not in audit:
            errors.append(f"coverage audit does not mention {journal}")

    doi_values = [normalize_doi(x) for x in re.findall(r"https?://doi\.org/(10\.\d{4,9}/[^\s)]+)", text, re.I)]
    main_text = text.split("## 2星观察区", 1)[0]
    observation = text.split("## 2星观察区", 1)[1].split("## 覆盖审计", 1)[0] if "## 2星观察区" in text else ""
    if "（环境）" in observation:
        errors.append("environmental papers must not enter the observation section")
    # A paper may legitimately link the same DOI again under “官方来源”.  Only
    # the canonical DOI field identifies entries for the duplicate check.
    main_dois = [
        normalize_doi(x)
        for x in re.findall(r"^- DOI：\[[^]]+\]\(https?://doi\.org/(10\.\d{4,9}/[^\s)]+)\)", main_text, re.I | re.M)
    ]
    duplicate_main_dois = sorted({doi for doi in main_dois if main_dois.count(doi) > 1})
    if duplicate_main_dois:
        errors.append(f"duplicate DOI in main list: {duplicate_main_dois}")

    # Accept both legacy all-bold headings and selectively bold author names.
    entry_re = re.compile(r"^\*\*\d+\.(?:\*\*)?\s+(.+)$", re.M)
    titles = [normalize_title(x) for x in entry_re.findall(main_text)]
    duplicate_titles = sorted({title for title in titles if titles.count(title) > 1})
    if duplicate_titles:
        errors.append(f"duplicate main entry heading: {duplicate_titles}")

    if "Abstract（原文摘录）" in main_text or "Abstract 核验片段" in main_text:
        errors.append("legacy abstract excerpt label found; use exactly `Abstract：`")

    blocks = re.split(r"(?=^\*\*\d+\.)", main_text, flags=re.M)[1:]
    for idx, block in enumerate(blocks, 1):
        environment = "（环境）" in block.splitlines()[0]
        if scoring_v2:
            components = []
            for label, limit in (("议题", 35), ("方法", 45), ("锚点", 10), ("延伸", 10)):
                component = re.search(rf"{label}\s*[：:]?\s*(\d+)\s*/\s*{limit}(?!\d)", block)
                if component:
                    components.append(int(component.group(1)))
            if len(components) != 4:
                errors.append(f"v2 entry {idx} requires topic/35, method/45, anchor/10, extension/10")
            else:
                try:
                    result = score_paper(*components, environment=environment)
                    total = re.search(r"总分\s*(\d+)\s*/\s*100", block)
                    rating = re.search(r"贴合度[：:]\s*(★+)", block)
                    if not total or int(total.group(1)) != result["final_total"]:
                        errors.append(f"v2 entry {idx} final total must be {result['final_total']} after gates")
                    if not rating or len(rating.group(1)) != result["stars"]:
                        errors.append(f"v2 entry {idx} stars inconsistent with gated score")
                    if result["placement"] != "main":
                        errors.append(f"v2 entry {idx} fails main-list admission")
                except ValueError as exc:
                    errors.append(f"v2 entry {idx}: {exc}")
            if not re.search(r"[｜|]\s*方法[：:]\s*[^｜|\n]+", block):
                errors.append(f"v2 entry {idx} missing method type in direction line")
        elif environment:
            rating = re.search(r"贴合度[：:]\s*(★+)", block)
            if not rating or len(rating.group(1)) not in (4, 5):
                errors.append(f"environmental entry {idx} must be four or five stars")
            score = re.search(r"(?:总分\s*)?(\d+)\s*/\s*100", block)
            topic = re.search(r"议题(?:命中度|命中|分)?\s*[：:]?\s*(\d+)", block)
            if not score or int(score.group(1)) < 70:
                errors.append(f"environmental entry {idx} requires total >= 70")
            if not topic or int(topic.group(1)) < 35:
                errors.append(f"environmental entry {idx} requires topic fit >= 35")
        for field in ["- DOI：", "- 方向：", "- Abstract：", "- 官方来源：", "- 直白解释："]:
            if field not in block:
                errors.append(f"main entry {idx} missing {field}")
        abstract = re.search(r"^- Abstract：(.+)$", block, re.M)
        if abstract and "摘要暂缺" not in abstract.group(1):
            if cjk_count(abstract.group(1)) < 80:
                errors.append(f"main entry {idx} abstract is too short to be a complete Chinese rendering")
            abstract_sentence_count = len(re.findall(r"[。！？!?]", abstract.group(1)))
            if abstract_sentence_count < 2:
                errors.append(f"main entry {idx} abstract has fewer than two sentences")
        if re.search(r"贴合度：★★(?!★)", block):
            errors.append(f"main entry {idx} is two-star; move it to observation section")
        explanation = re.search(r"^- 直白解释：(.+)$", block, re.M)
        if explanation:
            sentence_count = len(re.findall(r"[。！？!?]", explanation.group(1)))
            if sentence_count < 3:
                warnings.append(f"main entry {idx} plain explanation may have fewer than three sentences")
        if "- 中文摘要转述：" in block or "- Abstract（原文摘录）：" in block:
            errors.append(f"main entry {idx} contains a second or legacy abstract field; remove it")
        official_pos = block.rfind("- 官方来源：")
        explanation_pos = block.rfind("- 直白解释：")
        if official_pos < explanation_pos:
            errors.append(f"main entry {idx} official source must be the final field")

    if not doi_values:
        warnings.append("no DOI links detected")

    result = {
        "path": str(args.path),
        "main_entries": len(blocks),
        "scoring_version": "v2" if scoring_v2 else "legacy",
        "doi_links": len(doi_values),
        "errors": errors,
        "warnings": warnings,
        "ok": not errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
