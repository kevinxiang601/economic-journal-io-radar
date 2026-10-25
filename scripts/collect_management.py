#!/usr/bin/env python3
"""Discover UTD24 candidates without treating keyword hits as inclusion decisions."""
import argparse
import concurrent.futures
import datetime as dt
import json
import re
from pathlib import Path
import collect_candidates as common


def collect(journal: dict, since: dt.date, as_of: dt.date, openalex: bool,
            history_dois: set[str], history_titles: set[str]) -> dict:
    result = dict(journal=journal, errors=[], candidates=[], openalex_only=[])
    try:
        items = common.crossref_items(journal['issn'], since)
        result['crossref_count'] = len(items)
        for item in items:
            title = (item.get('title') or [''])[0]
            if re.search(r'^(correction|erratum|front matter|back matter|issue information|editorial)',title,re.I):
                continue
            online=common.date_parts(item,'published-online')
            created=common.date_parts(item,'created')
            abstract=common.strip_tags(item.get('abstract'))
            doi=common.normalize_doi(item.get('DOI'))
            seen_by=[]
            if doi in history_dois: seen_by.append('doi')
            if common.normalize_title(title) in history_titles: seen_by.append('title')
            result['candidates'].append(dict(
                journal=journal['code'],doi=doi,title=title,
                historical_duplicate=bool(seen_by),historical_match_by=seen_by,
                authors=[common.author_name(a) for a in item.get('author',[])],
                online=online,created=created,issued=common.date_parts(item,'issued'),
                printed=common.date_parts(item,'published-print'),
                in_window=bool(online and since.isoformat()<=online<=as_of.isoformat()),
                abstract=abstract,volume=item.get('volume'),issue=item.get('issue'),page=item.get('page'),
                topic_hints=common.topical_hits(title,abstract),links=item.get('link',[]),url=item.get('URL')))
    except Exception as exc:
        result['errors'].append('Crossref: '+str(exc))
    if openalex:
        try:
            oa=common.openalex_items(journal['issn'],since)
            result['openalex_count']=len(oa)
            found={p['doi'] for p in result['candidates']}
            result['openalex_only']=[p for p in oa if common.normalize_doi(p.get('doi')) not in found]
        except Exception as exc:
            result['errors'].append('OpenAlex: '+str(exc))
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--as-of',required=True)
    parser.add_argument('--lookback',type=int,default=45)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--openalex',action='store_true')
    parser.add_argument('--history-dir',type=Path,action='append',default=[])
    args=parser.parse_args()
    end=dt.date.fromisoformat(args.as_of); since=end-dt.timedelta(days=args.lookback)
    journals=json.loads((Path(__file__).parent.parent/'references/management-journals.json').read_text())
    history_dois,history_titles,history_files=set(),set(),[]
    for directory in args.history_dir:
        ds,ts,fs=common.parse_history(directory)
        history_dois.update(ds);history_titles.update(ts);history_files.extend(fs)
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        jobs={pool.submit(collect,j,since,end,args.openalex,history_dois,history_titles):j for j in journals}
        for job in concurrent.futures.as_completed(jobs):
            result=job.result();results.append(result)
            # Checkpoint partial, generated network data to the specified working file.
            args.output.write_text(json.dumps(dict(as_of=end.isoformat(),since=since.isoformat(),
                history=dict(files=history_files,doi_count=len(history_dois),title_count=len(history_titles)),
                journals=results),ensure_ascii=False,indent=2))
            print(result['journal']['code'],len(result['candidates']),result['errors'],flush=True)
    print('Completed',len(results),'journals;',sum(len(r['candidates']) for r in results),'candidates')


if __name__=='__main__':
    main()
