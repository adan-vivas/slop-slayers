#!/usr/bin/env python3
"""Verify a minimal Agent Skills repository without third-party dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'conceptual-interaction-design' / 'SKILL.md'
errors = []
if not SKILL.exists():
    errors.append(f'missing {SKILL}')
else:
    content=SKILL.read_text(encoding='utf-8')
    match=re.match(r'\A---\s*\n(.*?)\n---\s*\n', content, re.S)
    if not match:
        errors.append('SKILL.md missing YAML frontmatter')
    else:
        front=match.group(1)
        values={}
        for line in front.splitlines():
            if ':' in line and not line.startswith(' '):
                k, v=line.split(':',1)
                values[k.strip()] = v.strip()
        name=values.get('name','')
        desc=values.get('description','')
        if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64:
            errors.append('invalid name')
        if not desc or len(desc)>1024:
            errors.append('invalid description')
        if len(content.splitlines()) > 500:
            errors.append('SKILL.md > 500 lines')
    for label, target in re.findall(r'\[([^]]+)\]\(([^)]+)\)', content):
        if target.startswith(('https://','http://','#')):
            continue
        dest=(SKILL.parent / target.split('#',1)[0]).resolve()
        if not dest.is_file():
            errors.append(f'broken local reference: {target}')
for required in ['README.md','LICENSE','evals/rubric.md','evals/README.md']:
    if not (ROOT / required).is_file():
        errors.append(f'missing {required}')
case_count=len(list((ROOT/'evals'/'cases').glob('*.md')))
if case_count < 5:
    errors.append(f'only {case_count} evaluation cases')
if errors:
    print('VALIDATION FAILED')
    for e in errors: print(' -',e)
    sys.exit(1)
print(f'PASS: skill format, local file links, repo layout, and {case_count} evaluation cases')
print('NOTE: this is format validation, not UX outcome evaluation.')
