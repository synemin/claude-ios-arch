#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK = ROOT / 'manifests' / 'plugin-framework.json'


def main() -> int:
    data = json.loads(FRAMEWORK.read_text())
    bad = 0
    print('# Plugin Framework Audit')
    for layer in data.get('layers', []):
        missing = []
        for rel in layer.get('required', []):
            if not (ROOT / rel).exists():
                missing.append(rel)
        status = 'OK' if not missing else 'MISSING'
        print(f"## {layer['id']} — {status}")
        if missing:
            bad += len(missing)
            for rel in missing:
                print(f'- MISSING {rel}')
        else:
            for rel in layer.get('required', []):
                print(f'- OK {rel}')
    return 1 if bad else 0


if __name__ == '__main__':
    raise SystemExit(main())
