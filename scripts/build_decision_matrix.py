#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCORECARDS = ROOT / 'platforms' / 'ios' / 'scorecards'


def main():
    print('Decision topics:')
    for path in sorted(SCORECARDS.glob('*.md')):
        print(f'- {path.stem}')


if __name__ == '__main__':
    main()
