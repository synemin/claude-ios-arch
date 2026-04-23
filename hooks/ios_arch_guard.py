#!/usr/bin/env python3
"""Lightweight architecture guard script for iOS repositories.

Usage:
  python3 hooks/ios_arch_guard.py /path/to/repo

The script emits heuristic warnings for common low-debt violations:
- Manager/Helper/Util naming sprawl
- DTOs referenced in Views/ViewControllers
- Network calls inside Views/ViewControllers
- Catch-all Utils/Helpers/Common directories
"""

from __future__ import annotations
import pathlib
import re
import sys

FORBIDDEN_DIRS = {'Utils', 'Helpers', 'Common'}
TYPE_NAME_PATTERNS = [r'\b\w+Manager\b', r'\b\w+Helper\b', r'\b\w+Util\b']
VIEW_FILE_HINTS = ('View.swift', 'ViewController.swift')
NETWORK_HINTS = ('URLSession', '.dataTask', '.upload', '.download', 'Alamofire')
DTO_HINT = 'DTO'


def scan_file(path: pathlib.Path):
    warnings = []
    text = path.read_text(errors='ignore')
    for patt in TYPE_NAME_PATTERNS:
        for m in re.finditer(patt, text):
            warnings.append(f'{path}: generic type name {m.group(0)}')
    if any(path.name.endswith(h) for h in VIEW_FILE_HINTS):
        if DTO_HINT in text:
            warnings.append(f'{path}: DTO referenced in presentation file')
        if any(h in text for h in NETWORK_HINTS):
            warnings.append(f'{path}: network API referenced in presentation file')
    return warnings


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    warnings = []
    for p in root.rglob('*'):
        if p.is_dir() and p.name in FORBIDDEN_DIRS:
            warnings.append(f'{p}: catch-all directory detected')
        if p.is_file() and p.suffix == '.swift':
            warnings.extend(scan_file(p))
    if warnings:
        print('iOS architecture guard warnings:')
        for w in warnings:
            print('-', w)
        sys.exit(1)
    print('No heuristic architecture guard warnings found.')


if __name__ == '__main__':
    main()
