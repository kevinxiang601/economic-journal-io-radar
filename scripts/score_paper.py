#!/usr/bin/env python3
"""Compute v2 reading-priority scores after evidence-based human/agent assessment."""

import argparse
import json


def score_paper(topic: int, method: int, anchor: int, extension: int,
                environment: bool = False) -> dict:
    values = (topic, method, anchor, extension)
    limits = (35, 45, 10, 10)
    if any(type(v) is not int or not 0 <= v <= limit
           for v, limit in zip(values, limits)):
        raise ValueError("v2 integer ranges: topic 0–35, method 0–45, anchor/extension 0–10")
    raw = sum(values)
    cap = 100
    reasons = []
    for topic_min, method_min, limit in ((18, 20, 54), (24, 28, 69), (28, 36, 84)):
        if topic < topic_min or method < method_min:
            cap = min(cap, limit)
            reasons.append(f"topic < {topic_min} or method < {method_min}: cap {limit}")
    final = min(raw, cap)
    stars = 5 if final >= 85 else 4 if final >= 70 else 3 if final >= 55 else 2 if final >= 40 else 1
    if environment:
        placement = "main" if topic >= 31 and method >= 28 and final >= 70 else "exclude"
    else:
        placement = "main" if stars >= 3 else "optional_observation" if stars == 2 else "exclude"
    return dict(version="v2", raw_total=raw, final_total=final, stars=stars,
                cap=cap, cap_reasons=reasons, placement=placement)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("topic", "method", "anchor", "extension"):
        parser.add_argument(f"--{name}", type=int, required=True)
    parser.add_argument("--environment", action="store_true")
    args = parser.parse_args()
    try:
        result = score_paper(args.topic, args.method, args.anchor, args.extension, args.environment)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
