---
name: conceptual-interaction-design
description: Model software concepts, domain nouns and verbs, semantic grammar, states, and relationships before choosing interface components. Use for early-stage product design, information architecture, interaction design, feature redesign, AI-native workflows, and reviewing a proposed UI for conceptual coherence. Do not use for pure visual polish or narrowly specified UI implementation unless the underlying model is in question.
---

# Conceptual Interaction Design

## Purpose

Help the user discover **what the product is and how it behaves** before deciding **how its interface is rendered**. Treat the model as a falsifiable proposal, not truth about user intentions. A screen, card, graph, modal, folder, or dashboard is not automatically a domain concept.

**Operating rule:** Explain product behavior using domain objects, actions, states, and constraints without mentioning UI widgets. Only afterward map those behaviors to interaction patterns. If the user explicitly needs a quick implementation, do a proportionate conceptual pass rather than blocking progress.

## Workflow

### 0 — Establish scope and evidence

- Restate user goal, focal task, audience, and product context in one paragraph.
- Separate **Observed / Given**, **Inferred**, and **Unknown**. Never invent research evidence or private user intent.
- Identify whether the task requires a new model, reviewing an existing model, or comparing interaction options.
- For complex tasks consult [references/concept-design.md](references/concept-design.md), [references/semantic-grammar.md](references/semantic-grammar.md), and [references/object-modeling.md](references/object-modeling.md).

### 1 — Inventory candidate concepts (nouns)

For each candidate concept define:

| Field | Question |
|---|---|
| Purpose | What distinctive user benefit does this concept provide? |
| Identity | How does one instance differ from another? |
| State | What changes during its life? |
| Actions | What do people or systems do with it? |
| Relationships | What other concepts can it relate to, and how many? |
| Operational principle | What short, concrete scenario shows this concept creating value? |

- Reject candidates that are only views/containers without independent conceptual purpose; or justify why a container is itself a real concept.
- Merge redundant concepts when they offer indistinguishable value; split overloaded concepts where their lifecycles or invariants differ.
- Do not assume a physical/technical artifact (tab, file, database record) is the user's primary conceptual object.

### 2 — Identify verbs and actor boundaries

- List actions in domain language, distinguishing user intent from low-level UI operations.
- Assign actor: person, system, AI assistant, administrator, third party.
- For every important action include preconditions, state effects, error cases, and inverse/undo where possible.
- AI-generated associations must specify confidence/uncertainty, user override, provenance, and correction behavior when applicable.

### 3 — Write the semantic grammar

- Create an **object-action matrix** with allowed, conditional, forbidden, and not-applicable cells.
- Record cardinality (1:1, 1:n, m:n), ownership, containment versus reference, and cross-concept dependencies.
- Define state transitions and invariants. Explicitly test empty states, duplicates, conflicting edits, stale inferences, and deletion/archiving distinctions.
- Add one example operational scenario and one adversarial counterexample.
- Prefer compact structures; never add a concept merely to make a prettier diagram.

### 4 — Critique the model before UI

Challenge:
1. Can users predict what each action changes?
2. Can a user explain why each concept is distinct?
3. Can a concept function independently or is it an accidental implementation detail?
4. Does the model contradict itself on ownership, identity, lifecycle, or access?
5. Is it possible to recover from errors and reverse surprising changes?
6. Is uncertainty expressed honestly rather than turned into invented intent?
7. What evidence would falsify the proposed model?

Give a short revision list with priority and tradeoffs. Consult [references/concept-design.md](references/concept-design.md).

### 5 — Generate genuinely different interaction models

Only after the grammar is stable enough:
- Generate two or three approaches with **different organizing principles**, not superficial layouts of the same model.
- Explain the relationship between model and representation, core user journey, primary actions, and weaknesses of each.
- Evaluate discoverability, cognitive load, continuity, reversibility, access needs, and application posture; consult [references/interaction-principles.md](references/interaction-principles.md).
- Consider spatial layers/motion only when they improve orientation and cause-and-effect, not merely aesthetics; consult [references/spatial-and-motion.md](references/spatial-and-motion.md).
- Justify major UI widgets by a named model constraint or operation. Do not default to modals, dashboards, graphs, timelines, sidebars, cards, or canvases.

### 6 — Validate the proposal

- Separate conceptual coherence (reasoned argument) from empirical usability (requires studies).
- Propose concrete tasks and observations that could distinguish the competing models.
- Surface open decisions and assumptions that need user research, prototypes, or technical feasibility tests.

## Deliverables (adapt to task size)

1. **Domain definition** (one paragraph and evidence caveat)
2. **Concept inventory** (purpose, state, actions, operational principles)
3. **Object-action matrix** and **relationship/transition rules**
4. **Conceptual critique** (ambiguities and alternatives)
5. **Interaction-model comparison** (two+ when exploring)
6. **Recommendation** with tradeoffs and test plan

Use [templates/concept-inventory.md](templates/concept-inventory.md), [templates/object-action-matrix.md](templates/object-action-matrix.md), and [templates/interaction-model-review.md](templates/interaction-model-review.md) as optional output scaffolds. Avoid forcing verbose artifacts onto simple questions.

## Safety and source discipline

- Do not copy proprietary book text or imply the original authors endorse this synthesis.
- For academic claims, distinguish source-supported principles from original extrapolations; see [references/source-map.md](references/source-map.md).
- Treat AI understanding of user intent as hypothetical until supported. Preserve user control and correction pathways.
- Do not silently reframe an audience or product goal. Ask only when essential; otherwise state an assumption and continue.
