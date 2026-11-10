# Semantic grammar — synthesized from Daniel Rosenberg

**Source anchor:** [Rosenfeld workshop outline](https://rosenfeldmedia.com/rosenfeld-workshops/workshop/interaction-design-10x-faster-10x-better/) and [World IA Day talk page](https://www.worldiaday.org/talks/leveraging-information-architecture-within-ux-interaction-design-daniel-rosenberg).

The workshop explicitly distinguishes a grammar/conceptual layer from the design-pattern selection layer. The steps below are a practical synthesis, not copied course materials.

## Build grammar without widgets

1. Objects: label entities in user-facing domain terms.
2. Operations: pair each object with only the actions it supports.
3. Attributes: distinguish editable state, immutable identity, derived properties, and AI-inferred claims.
4. Constraints: express permissions, cardinality, and lifecycle rules as explicit sentences.
5. Cross-object flows: what actions move from one object to another without a conceptual gap?

## Object-action matrix

Rows are objects; columns are verbs. Cell status:
- `A` available to actor
- `C` conditional (state / permission)
- `F` forbidden (business invariant)
- `—` not applicable

For each `C`, state the condition. For each destructive action, document recovery. A sparse matrix is **not automatically** cognitively optimal: investigate whether sparsity reflects clear responsibilities or omitted capabilities.

## Mapping to patterns (later)

Ask of each candidate pattern: which operation does it expose, what is visible during the operation, how do users reverse it, and how does it help maintain orientation? A modal is sometimes justified (e.g. interruption necessary for destructive confirmation), but is never a default substitute for deciding the semantics.
