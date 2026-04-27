#!/usr/bin/env python3
from __future__ import annotations
import json
from datetime import date, datetime
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'references' / 'registry.json'
TODAY = date.today()
DATE_RE = re.compile(r'^Last reviewed:\s*(\d{4}-\d{2}-\d{2})$', re.MULTILINE)


def parse_review_date(text: str):
    m = DATE_RE.search(text)
    if not m:
        return None
    return datetime.strptime(m.group(1), '%Y-%m-%d').date()


def main():
    data = json.loads(REGISTRY.read_text())
    bad = 0
    for source in data.get('sources', []):
        cadence = source.get('reviewCadenceDays', 90)
        for rel in source.get('ownedReferences', []):
            path = ROOT / rel
            if not path.exists():
                print(f'MISSING {rel}')
                bad += 1
                continue
            reviewed = parse_review_date(path.read_text())
            if reviewed is None:
                print(f'NO_DATE {rel}')
                bad += 1
                continue
            age = (TODAY - reviewed).days
            status = 'STALE' if age > cadence else 'OK'
            print(f'{status} {rel} age={age}d cadence={cadence}d')
            if age > cadence:
                bad += 1
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
