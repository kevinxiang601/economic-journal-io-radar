#!/usr/bin/env python3
"""Choose alternating weekly track by calendar, never by previous run success."""
import argparse
import datetime as dt
import json


def select_track(date: dt.date, anchor: dt.date = dt.date(2026, 10, 26)) -> str:
    if anchor.weekday() != 0:
        raise ValueError('anchor must be a Monday economics week')
    return 'economics' if ((date-anchor).days // 7) % 2 == 0 else 'management'


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--date',required=True)
    p.add_argument('--anchor',default='2026-10-26')
    a=p.parse_args()
    day=dt.date.fromisoformat(a.date);anchor=dt.date.fromisoformat(a.anchor)
    print(json.dumps(dict(date=str(day),anchor=str(anchor),track=select_track(day,anchor))))
