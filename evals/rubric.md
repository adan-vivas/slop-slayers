# Blind evaluator rubric — 0 to 4 per dimension

Use integers, relative to the prompt's actual needs. Score 0 = absent/incorrect; 1 = weak; 2 = adequate; 3 = strong; 4 = exceptional and precise.

1. `concept_purpose` — Each main concept has a distinctive user-facing purpose; avoids conflating UI containers with domain entities.
2. `grammar_consistency` — Object-action permissions, cardinality, invariants, and lifecycle are coherent.
3. `edge_cases` — Addresses ambiguity, duplicates, empty states, failure, deletion/recovery, and AI uncertainty where applicable.
4. `interaction_diversity` — Produces meaningfully distinct interaction models rather than cosmetic layout variants, when the case requests multiple options.
5. `component_justification` — Interface choices derive from named user actions/constraints, not stock patterns.
6. `user_control` — Feedback, reversibility, accessibility, and corrections are explicit and appropriate.
7. `evidence_honesty` — Clearly separates given facts, assumptions, and testable hypotheses; does not fabricate user research.

Useful qualitative fields (store in separate reviewer notes): most consequential missing rule; best novel insight; worst premature component; recommendation verdict. Do not score verbosity as intrinsic quality.
