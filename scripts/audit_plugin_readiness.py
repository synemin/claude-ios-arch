#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    'docs': [
        'docs/PRODUCT-REQUIREMENTS.md',
        'docs/INSTALL.md',
        'docs/USAGE.md',
        'docs/WORKFLOW-MODEL.md',
    ],
    'state-and-platform': [
        'platforms/ios/guide.md',
        'platforms/ios/state-detection.md',
        'platforms/ios/architecture-evolution.md',
    ],
    'manifests': [
        'plugin/manifest.json',
        'core/manifest.json',
        'manifests/capabilities.json',
        'manifests/decision-topics.json',
        'manifests/project-states.json',
        'references/registry.json',
    ],
    'workflows': [
        'workflows/docs-refresh.md',
        'workflows/reference-review.md',
        'workflows/skill-regeneration.md',
        'workflows/release-audit.md',
    ],
}


def main():
    bad = 0
    print('# Plugin Readiness Audit')
    for group, paths in REQUIRED.items():
        print(f'## {group}')
        for rel in paths:
            path = ROOT / rel
            if path.exists():
                print(f'OK {rel}')
            else:
                print(f'MISSING {rel}')
                bad += 1
    print('## counts')
    print('commands', len(list((ROOT/'commands').glob('*.md'))))
    print('skills', len(list((ROOT/'skills').rglob('SKILL.md'))))
    print('references', len([p for p in (ROOT/'references').rglob('*') if p.is_file()]))
    print('examples', len(list((ROOT/'examples').glob('*.md'))))
    print('templates', len(list((ROOT/'templates').glob('*.md'))))
    print('scorecards', len(list((ROOT/'platforms'/'ios'/'scorecards').glob('*.md'))))
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
