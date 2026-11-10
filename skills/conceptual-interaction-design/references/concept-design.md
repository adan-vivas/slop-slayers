# Concept design — synthesized from Daniel Jackson

**Source anchor:** [Daniel Jackson, *The Essence of Software*](https://press.princeton.edu/books/hardcover/9780691225388/the-essence-of-software); [author's operational-principle explanation](https://essenceofsoftware.com/drafts/concepts-redux/the-operational-principle/).

This reference translates publicly described ideas into an original, actionable checklist. It is not a replacement for the full book.

## Operational method

A concept is more useful than a generic noun when it describes an autonomous service or capability with recognizable value. For each candidate:

1. **Purpose test:** complete "People use [concept] in order to [specific outcome]." Reject broad purposes such as "manage data."
2. **State test:** list persistent, meaningful state changes; if none exist, consider whether the noun is an attribute or derived view rather than concept.
3. **Action test:** enumerate meaningful operations with effects; exclude implementation-only operations.
4. **Operational principle:** write a short, representative scenario that makes the mechanism and value understandable without UI specifics.
5. **Independence test:** can this concept be described without assuming a specific widget or a tightly coupled neighboring feature?
6. **Composition test:** how does it interact with other concepts, and what coupling or leakage emerges?

## Challenge patterns

- **False concept:** a Dashboard or Page with no independent behavioral identity.
- **Overloaded concept:** one object mixes content, notification, ownership, and workflow with separate lifecycles.
- **Redundant concept:** Folder and Group both offer nearly identical containment semantics without reason.
- **History trap:** chronologically ordered events masquerade as a model of user goals.
- **Inference trap:** system assigns an intention without evidence and presents it as fact.

## Output: concept card

```
Concept: [name]
Purpose: [user outcome]
Identity: [distinguishing fields or condition]
State: [meaningful lifecycle]
Actions: [actor : verb -> effect]
Relationships: [other concept, cardinality, meaning]
Operational principle: [short scenario]
Failure/invariant: [what may never happen]
Open question: [uncertainty]
```
