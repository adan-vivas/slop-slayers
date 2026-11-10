# Evaluation protocol — paired, blind rubric comparison

This suite is an **evaluation scaffold**, not a claim that the skill improves agent performance. Do not treat script validation as a usability study.

## Cases

1. `cases/rabbit-hole.md` — nonlinear research and inferred intent
2. `cases/appointment-scheduler.md` — scheduling states and contention
3. `cases/community-knowledge.md` — contributions, identity, moderation
4. `cases/team-decisions.md` — decisions, evidence, reversals
5. `cases/smart-home.md` — control, permissions, and safety boundaries

## Paired test

For each case, run the **same agent/model and task** twice in isolated chats with identical input:
- **baseline**: ordinary prompting, no skill loaded
- **skill**: skill active and references available

Vary order across cases if practical. Save raw outputs, model/version, temperature/thinking settings, date, and tool context. Do not let baseline see skill instructions. Repeat with multiple seeds/models when possible.

## Blind scoring

Have a reviewer who doesn't know which condition produced which output score each dimension in [rubric.md](rubric.md) from 0–4. Use two independent raters if available and resolve disagreements explicitly. The reviewer should also identify practical failures rather than relying only on numeric scores. Proposed human usability still needs tests with actual users.

Create `scores.csv` with header:

```csv
case,condition,dimension,score
```

Each case/condition should include all 7 rubric dimensions, with integer 0–4. Save outputs in `outputs/` locally (not required in GitHub).

```bash
python3 scripts/score_evals.py evals/scores.csv
```

The scorer checks coverage and prints averages and differences. It does **not** generate model responses or perform judgment automatically.

## Release gate suggestion

Before calling v1.0 validated, require: 5 paired cases, two reviewers, no significant unaddressed failure mode, and a documented comparison that demonstrates beneficial differences on difficult conceptual cases. These are project criteria, not established scientific validity.
