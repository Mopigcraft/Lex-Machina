#!/usr/bin/env python3
"""Build one installable ZIP per skill from an unpacked skills tree.

Replaces the ZIP folders that used to be committed to the repository: archives
are now built on demand (locally or by the release workflow) and published as
GitHub Release assets.

Before packaging, every skill's CHECKSUMS.sha256 is checked against its files;
a stale or incomplete manifest stops the build. Plugin-channel files at the
skill root (`.claude-plugin/`, `.mcp.json`) and `__pycache__` are left out of
the ZIP: claude.ai rejects a skill upload that carries a plugin manifest.
Every archive is verified byte-for-byte against the tree after writing.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from verify_development_archives import verify

FIXED_DT = (1980, 1, 1, 0, 0, 0)


def check_manifest(skill):
    """Return errors for CHECKSUMS.sha256 vs files actually present."""
    manifest = skill / 'CHECKSUMS.sha256'
    if not manifest.is_file():
        return [f'{skill.name}: missing CHECKSUMS.sha256']
    expected = {}
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        digest, rel = line.split(None, 1)
        expected[rel.strip().removeprefix('./')] = digest.lower()
    actual = {p.relative_to(skill).as_posix(): p for p in skill.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts
              and p.relative_to(skill).as_posix() != 'CHECKSUMS.sha256'}
    errors = [f'{skill.name}: not in CHECKSUMS.sha256: {n}'
              for n in sorted(actual.keys() - expected.keys())]
    errors += [f'{skill.name}: listed but missing: {n}'
               for n in sorted(expected.keys() - actual.keys())]
    for n in sorted(actual.keys() & expected.keys()):
        if hashlib.sha256(actual[n].read_bytes()).hexdigest() != expected[n]:
            errors.append(f'{skill.name}: SHA-256 mismatch: {n}')
    return errors


def build(source, out):
    skills = sorted(p for p in source.iterdir()
                    if p.is_dir() and (p / 'SKILL.md').is_file())
    if not skills:
        raise SystemExit(f'No skills found in {source}')
    errors = [e for s in skills for e in check_manifest(s)]
    if errors:
        raise SystemExit('\n'.join(errors))
    out.mkdir(parents=True, exist_ok=True)
    if any(out.glob('*.zip')):
        raise SystemExit(f'{out} already contains ZIPs; use an empty directory')
    for skill in skills:
        paths = sorted(p for p in skill.rglob('*')
                       if p.is_file()
                       and not p.relative_to(skill).parts[0].startswith('.')
                       and '__pycache__' not in p.parts)
        if any(p.is_symlink() for p in paths):
            raise SystemExit(f'Symlink in source: {skill}')
        with ZipFile(out / f'{skill.name}.zip', 'w', ZIP_DEFLATED,
                     compresslevel=9) as zf:
            for path in paths:
                info = ZipInfo(path.relative_to(source).as_posix(), date_time=FIXED_DT)
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = ZIP_DEFLATED
                zf.writestr(info, path.read_bytes(), compresslevel=9)
    report = verify(out, source)
    if report['errors']:
        raise SystemExit('\n'.join(report['errors']))
    sums = ''.join(f"{p['sha256']}  {p['archive']}\n" for p in report['packages'])
    (out / 'SHA256SUMS').write_text(sums, encoding='utf-8', newline='\n')
    return {'packages': len(report['packages']),
            'files': sum(p['files'] for p in report['packages'])}


def main():
    repo = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--source', type=Path,
                        default=repo / 'Wersja rozwojowa rozpakowana')
    parser.add_argument('--out', type=Path, default=repo / 'dist-zips')
    args = parser.parse_args()
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    print(json.dumps(build(args.source, args.out), indent=2))


if __name__ == '__main__':
    main()
