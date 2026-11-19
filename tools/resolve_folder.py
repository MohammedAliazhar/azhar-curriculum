#!/usr/bin/env python3
"""Resolve the target lecture folder path given a BATCH-ID and Session Name.

Usage:
    python3 tools/resolve_folder.py "BATCH-ID" "Session Name"
"""
import sys
import os
import re
import difflib

def slugify(text):
    text = re.sub(r'^\s*(\d+(\.\d+)?|\d+\s*-\s*\d+(\.\d+)?|Session\s*\d+(\.\d+)?|Academic\s*session\s*\d+(\.\d+)?|\d+)\s*[-:]*\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'[\(\)]', '', text)
    text = text.replace('&', 'and')
    s = re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()
    return s

def resolve_folder(batch_id, session_name):
    if not os.path.isdir(batch_id):
        print(f"Error: Batch directory '{batch_id}' not found.", file=sys.stderr)
        sys.exit(1)

    target_slug = slugify(session_name)
    candidates = []

    for mod in sorted(os.listdir(batch_id)):
        mp = os.path.join(batch_id, mod)
        if not os.path.isdir(mp):
            continue
        for lec in sorted(os.listdir(mp)):
            lp = os.path.join(mp, lec)
            if not os.path.isdir(lp) or not lec.startswith('lecture-'):
                continue
            lec_slug = re.sub(r'^lecture-\d+-', '', lec)
            candidates.append((lp, lec_slug))
            if target_slug == lec_slug or target_slug in lec_slug or lec_slug in target_slug:
                return lp

    # Fuzzy match
    slugs = [c[1] for c in candidates]
    matches = difflib.get_close_matches(target_slug, slugs, n=1, cutoff=0.5)
    if matches:
        for lp, s in candidates:
            if s == matches[0]:
                return lp

    print(f"Error: Could not resolve lecture folder for session '{session_name}' in batch '{batch_id}'.", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 tools/resolve_folder.py <BATCH-ID> <Session Name>", file=sys.stderr)
        sys.exit(1)

    batch_arg = sys.argv[1].strip()
    session_arg = sys.argv[2].strip()
    result = resolve_folder(batch_arg, session_arg)
    print(result.replace("\\", "/"))
