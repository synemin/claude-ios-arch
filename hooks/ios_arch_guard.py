#!/usr/bin/env python3
"""Heuristic architecture guard for iOS repositories.

Usage:
  python3 hooks/ios_arch_guard.py /path/to/repo

Output style is agent-friendly:
- severity-tagged findings
- issue code
- path
- message

Current heuristic checks:
- generic Manager/Helper/Util naming
- DTO leakage into Views/ViewControllers/ViewModels
- network calls inside presentation files
- catch-all Utils/Helpers/Common directories
- oversized ViewModel classes
- missing feature-first structure hints in larger repos
- likely singleton sprawl
- missing composition root hints in larger repos
- weak observability signal in larger repos
- callback-heavy async legacy signal
"""

from __future__ import annotations
import pathlib
import re
import sys

FORBIDDEN_DIRS = {'Utils', 'Helpers', 'Common'}
GENERIC_TYPE_PATTERNS = [r'\w+Manager', r'\w+Helper', r'\w+Util']
PRESENTATION_HINTS = ('View.swift', 'ViewController.swift', 'ViewModel.swift')
VIEW_ONLY_HINTS = ('View.swift', 'ViewController.swift')
NETWORK_HINTS = ('URLSession', '.dataTask', '.upload', '.download', 'Alamofire')
DTO_HINT = 'DTO'
FEATURE_DIR_NAMES = {'Features', 'Feature'}
VIEWMODEL_SIZE_LINES = 250
LOGGING_HINTS = ('Logger(', 'os_log', 'OSLog', 'Crashlytics', 'SentrySDK', 'analytics.track', 'logEvent(')
COMPOSITION_ROOT_HINTS = ('AppEnvironment', 'AppBootstrap', 'DependencyContainer', 'CompositionRoot')
CALLBACK_HINTS = ('completion:', '@escaping', 'DispatchQueue.main.async')
SINGLETON_HINT = '.shared'


def add_finding(findings, severity, code, path, message):
    findings.append({
        'severity': severity,
        'code': code,
        'path': str(path),
        'message': message,
    })


def scan_file(path: pathlib.Path, findings):
    text = path.read_text(errors='ignore')
    lines = text.splitlines()

    for patt in GENERIC_TYPE_PATTERNS:
        for m in re.finditer(patt, text):
            add_finding(findings, 'S2', 'generic-name', path, f'generic type name {m.group(0)}')

    if text.count(SINGLETON_HINT) >= 3:
        add_finding(findings, 'S2', 'singleton-sprawl', path, 'multiple .shared usages suggest singleton-heavy design')

    if any(path.name.endswith(h) for h in PRESENTATION_HINTS):
        if DTO_HINT in text:
            sev = 'S1' if any(path.name.endswith(h) for h in VIEW_ONLY_HINTS) else 'S2'
            add_finding(findings, sev, 'dto-leakage', path, 'DTO referenced in presentation-layer file')
        if any(h in text for h in NETWORK_HINTS):
            sev = 'S1' if any(path.name.endswith(h) for h in VIEW_ONLY_HINTS) else 'S2'
            add_finding(findings, sev, 'presentation-networking', path, 'network API referenced in presentation-layer file')

    if path.name.endswith('ViewModel.swift') and len(lines) > VIEWMODEL_SIZE_LINES:
        add_finding(findings, 'S2', 'oversized-viewmodel', path, f'ViewModel has {len(lines)} lines (> {VIEWMODEL_SIZE_LINES})')

    if sum(text.count(h) for h in CALLBACK_HINTS) >= 5:
        add_finding(findings, 'S3', 'callback-heavy', path, 'file shows many callback-era async hints; review concurrency migration needs')


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    findings = []
    swift_files = 0
    feature_dir_present = False
    composition_root_present = False
    observability_hits = 0

    for p in root.rglob('*'):
        if p.is_dir() and p.name in FEATURE_DIR_NAMES:
            feature_dir_present = True
        if p.is_dir() and p.name in FORBIDDEN_DIRS:
            add_finding(findings, 'S2', 'catch-all-dir', p, 'catch-all directory detected')
        if p.is_file() and p.suffix == '.swift':
            swift_files += 1
            text = p.read_text(errors='ignore')
            if any(h in text or p.name.startswith(h) for h in COMPOSITION_ROOT_HINTS):
                composition_root_present = True
            observability_hits += sum(text.count(h) for h in LOGGING_HINTS)
            scan_file(p, findings)

    if swift_files >= 20 and not feature_dir_present:
        add_finding(findings, 'S3', 'no-feature-root', root, 'larger Swift repo without obvious feature-first root detected')

    if swift_files >= 20 and not composition_root_present:
        add_finding(findings, 'S3', 'no-composition-root-signal', root, 'larger Swift repo without obvious bootstrap/composition-root signal detected')

    if swift_files >= 20 and observability_hits == 0:
        add_finding(findings, 'S3', 'weak-observability-signal', root, 'larger Swift repo without obvious logging/analytics/crash signal detected')

    if findings:
        print('iOS architecture guard findings:')
        for f in findings:
            print(f"[{f['severity']}] {f['code']} | {f['path']} | {f['message']}")
        if any(f['severity'] in ('S1', 'S2') for f in findings):
            sys.exit(1)
        sys.exit(0)

    print('No heuristic architecture guard findings found.')


if __name__ == '__main__':
    main()
