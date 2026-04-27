#!/usr/bin/env python3
from __future__ import annotations
import argparse
import gzip
import io
import urllib.request


def main():
    p = argparse.ArgumentParser(description='Fetch an official source URL with urllib and print a text excerpt.')
    p.add_argument('url')
    p.add_argument('--bytes', type=int, default=8000)
    args = p.parse_args()

    req = urllib.request.Request(args.url, headers={
        'User-Agent': 'Mozilla/5.0',
        'Accept-Encoding': 'gzip',
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        enc = (r.headers.get('Content-Encoding') or '').lower()
        if enc == 'gzip' or raw[:2] == bytes([0x1f, 0x8b]):
            try:
                raw = gzip.GzipFile(fileobj=io.BytesIO(raw)).read()
            except Exception:
                pass
        text = raw.decode('utf-8', 'ignore')
        print(f'URL: {args.url}')
        print(f'Status: {getattr(r, "status", "?")}')
        print(text[:args.bytes])


if __name__ == '__main__':
    main()
