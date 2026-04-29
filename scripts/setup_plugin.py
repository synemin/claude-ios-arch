#!/usr/bin/env python3
from __future__ import annotations
import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / 'skills'

HOSTS = {
    'claude-code': {
        'skill_dir': Path.home() / '.claude' / 'skills',
        'adapter': ROOT / 'adapters' / 'claude-code' / 'CLAUDE.md',
        'project_instruction': 'CLAUDE.md',
    },
    'codex': {
        'skill_dir': Path.home() / '.codex' / 'skills',
        'adapter': ROOT / 'adapters' / 'codex' / 'AGENTS.md',
        'project_instruction': 'AGENTS.md',
    },
}

REQUIRED_SKILLS = [
    'ios-plugin-operations',
    'ios-app-bootstrap',
    'ios-existing-project-adoption',
    'ios-feature-implementation',
    'ios-arch-review',
    'ios-debt-check',
    'ios-architecture-evolution',
    'ios-tech-decision',
    'ios-tooling-decision',
    'ios-testing-strategy',
    'ios-library-selection',
    'ios-release-operations',
]


def fail(msg: str) -> int:
    print(f'ERROR {msg}', file=sys.stderr)
    return 1


def copy_skill(name: str, dest_root: Path, dry_run: bool) -> None:
    src = SKILLS_DIR / name
    dest = dest_root / name
    if not src.exists():
        raise FileNotFoundError(f'missing skill source: {src}')
    print(f"{'DRY-RUN ' if dry_run else ''}INSTALL {name} -> {dest}")
    if dry_run:
        return
    dest_root.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def verify_host(host: str, target_dir: Path | None = None) -> int:
    cfg = HOSTS[host]
    skill_root = target_dir or cfg['skill_dir']
    bad = 0
    print(f'# Verify {host}')
    print(f'skill_dir: {skill_root}')
    for name in REQUIRED_SKILLS:
        skill = skill_root / name / 'SKILL.md'
        if skill.exists():
            print(f'OK {name}')
        else:
            print(f'MISSING {name}')
            bad += 1
    adapter = cfg['adapter']
    print(f"adapter: {'OK' if adapter.exists() else 'MISSING'} {adapter}")
    if not adapter.exists():
        bad += 1
    return bad


def install_host(host: str, target_dir: Path | None, dry_run: bool) -> int:
    cfg = HOSTS[host]
    skill_root = target_dir or cfg['skill_dir']
    print(f'# Install {host}')
    print(f'skill_dir: {skill_root}')
    for name in REQUIRED_SKILLS:
        copy_skill(name, skill_root, dry_run)
    print('\nNext project instruction:')
    print(f"- Add or update {cfg['project_instruction']} to load this plugin adapter when working on iOS apps:")
    print(f"  {cfg['adapter']}")
    print('- Do not install Context7/MCP, LSP tools, signing assets, or global CLIs without explicit approval.')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description='Install or verify claude-ios-arch skills for Claude Code / Codex hosts.')
    parser.add_argument('--host', choices=[*HOSTS.keys(), 'all'], required=True)
    parser.add_argument('--verify', action='store_true', help='verify host skill installation instead of copying')
    parser.add_argument('--dry-run', action='store_true', help='show actions without writing')
    parser.add_argument('--target-dir', type=Path, help='override target skills directory, useful for tests')
    args = parser.parse_args()

    if not SKILLS_DIR.exists():
        return fail(f'missing skills directory: {SKILLS_DIR}')

    hosts = list(HOSTS) if args.host == 'all' else [args.host]
    failures = 0
    for host in hosts:
        if args.verify:
            failures += verify_host(host, args.target_dir)
        else:
            failures += install_host(host, args.target_dir, args.dry_run)
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
