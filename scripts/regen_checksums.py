#!/usr/bin/env python3
"""Regenerate CHECKSUMS.sha256 for skills in an unpacked skills tree.

Format (as checked by build_skill_zips.py and check_checksums.py / T21):
`<sha256>  ./<relpath>`, sorted by path, LF, trailing newline; every file of the
skill except CHECKSUMS.sha256 itself and __pycache__.

  python scripts/regen_checksums.py                 # all skills
  python scripts/regen_checksums.py shared dr-02-…  # selected skills
  python scripts/regen_checksums.py --check         # report stale manifests, exit 1
"""
import argparse
import hashlib
import sys
from pathlib import Path


def manifest(skill):
    files = sorted(p.relative_to(skill).as_posix() for p in skill.rglob('*')
                   if p.is_file() and '__pycache__' not in p.parts
                   and p.relative_to(skill).as_posix() != 'CHECKSUMS.sha256')
    return ''.join(f"{hashlib.sha256((skill / r).read_bytes()).hexdigest()}  ./{r}\n"
                   for r in files)


def main():
    repo = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('skills', nargs='*')
    parser.add_argument('--source', type=Path,
                        default=repo / 'Wersja rozwojowa rozpakowana')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    names = args.skills or sorted(p.name for p in args.source.iterdir()
                                  if (p / 'SKILL.md').is_file())
    stale = []
    for name in names:
        skill = args.source / name
        path = skill / 'CHECKSUMS.sha256'
        new = manifest(skill)
        old = path.read_text(encoding='utf-8') if path.is_file() else None
        if old == new:
            continue
        stale.append(name)
        if not args.check:
            path.write_text(new, encoding='utf-8', newline='\n')
    print(('stale: ' if args.check else 'updated: ') + (', '.join(stale) or 'none'))
    return 1 if args.check and stale else 0


if __name__ == '__main__':
    sys.exit(main())
