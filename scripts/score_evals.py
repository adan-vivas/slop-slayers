#!/usr/bin/env python3
"""Summarize manually scored baseline-vs-skill evaluations. Does not generate scores."""
from collections import defaultdict
from pathlib import Path
import csv
import sys

DIMS={'concept_purpose','grammar_consistency','edge_cases','interaction_diversity','component_justification','user_control','evidence_honesty'}
CONDS={'baseline','skill'}

def main(path):
    scores=defaultdict(dict)
    with Path(path).open(encoding='utf-8',newline='') as f:
        reader=csv.DictReader(f)
        if not {'case','condition','dimension','score'}.issubset(reader.fieldnames or []):
            raise ValueError('CSV must contain case, condition, dimension, score columns')
        for row in reader:
            case,condition,dim=row['case'].strip(),row['condition'].strip(),row['dimension'].strip()
            if not case or condition not in CONDS or dim not in DIMS:
                raise ValueError(f'bad case/condition/dimension in {row}')
            val=int(row['score'])
            if not 0<=val<=4: raise ValueError('scores must be 0–4')
            key=(case,condition)
            if dim in scores[key]: raise ValueError(f'duplicate dimension in {key}: {dim}')
            scores[key][dim]=val
    if not scores: raise ValueError('CSV contains no scores')
    cases=sorted({case for case,_ in scores})
    for case in cases:
        for cond in CONDS:
            missing=DIMS-set(scores.get((case,cond),{}))
            if missing: raise ValueError(f'missing {case}/{cond}: {sorted(missing)}')
    print('Dimension,baseline,skill,difference (skill - baseline)')
    for dim in sorted(DIMS):
        b=sum(scores[(c,'baseline')][dim] for c in cases)/len(cases)
        s=sum(scores[(c,'skill')][dim] for c in cases)/len(cases)
        print(f'{dim},{b:.2f},{s:.2f},{s-b:+.2f}')
    print(f'\nPaired cases: {len(cases)}. Scores are reviewer judgments, not objective UX proof.')

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print('Usage: python3 scripts/score_evals.py evals/scores.csv',file=sys.stderr)
        sys.exit(2)
    try: main(sys.argv[1])
    except (ValueError,OSError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr)
        sys.exit(1)
