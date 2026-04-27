#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / 'references' / 'registry.json'


def main():
    data = json.loads(REGISTRY.read_text())
    bad = 0
    for source in data.get('sources', []):
        for rel in source.get('ownedReferences', []):
            path = ROOT / rel
            if path.exists():
                print(f'OK {rel}')
            else:
                print(f'MISSING {rel}')
                bad += 1
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
