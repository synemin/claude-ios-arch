#!/usr/bin/env python3
from __future__ import annotations
import json
from datetime import date, datetime
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'references' / 'registry.json'
DATE_RE = re.compile(r'^Last reviewed:\s*(\d{4}-\d{2}-\d{2})$', re.MULTILINE)
TODAY = date.today()


def parse_review_date(text: str):
    m = DATE_RE.search(text)
    if not m:
        return None
    return datetime.strptime(m.group(1), '%Y-%m-%d').date()


def main():
    data = json.loads(REGISTRY.read_text())
    rows = []
    for source in data.get('sources', []):
        cadence = source.get('reviewCadenceDays', 90)
        for rel in source.get('ownedReferences', []):
            path = ROOT / rel
            reviewed = parse_review_date(path.read_text()) if path.exists() else None
            age = None if reviewed is None else (TODAY - reviewed).days
            due = path.exists() is False or reviewed is None or age > cadence
            rows.append({
                'source': source['id'],
                'topic': source.get('topic'),
                'reference': rel,
                'priority': source.get('priority', 'medium'),
                'cadenceDays': cadence,
                'ageDays': age,
                'due': due,
                'url': source.get('url'),
            })

    rows.sort(key=lambda r: (not r['due'], {'high':0,'medium':1,'low':2}.get(r['priority'], 9), r['reference']))
    print('# Refresh Report')
    print(f'date: {TODAY.isoformat()}')
    print()
    for row in rows:
        status = 'DUE' if row['due'] else 'OK '
        age = '?' if row['ageDays'] is None else str(row['ageDays'])
        print(f"- [{status}] {row['reference']} | source={row['source']} | priority={row['priority']} | age={age}d/{row['cadenceDays']}d")


if __name__ == '__main__':
    main()
