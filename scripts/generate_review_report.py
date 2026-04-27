#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CAPS = ROOT / 'manifests' / 'capabilities.json'
STATES = ROOT / 'manifests' / 'project-states.json'


def main():
    caps = json.loads(CAPS.read_text())
    states = json.loads(STATES.read_text())
    print('# Plugin Review Snapshot')
    print(f"phase: {caps.get('phase')}")
    print('capabilities:')
    for item in caps.get('capabilities', []):
        print(f'- {item}')
    print('project states:')
    for state in states.get('states', []):
        print(f"- {state['id']}: {state['description']}")


if __name__ == '__main__':
    main()
