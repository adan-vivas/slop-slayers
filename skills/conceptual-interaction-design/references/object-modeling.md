# Object-oriented product model — Johnson/Henderson + Sophia Prater

**Sources:** [Johnson & Henderson, *Conceptual Models*, Springer 2024](https://link.springer.com/book/10.1007/978-3-031-50852-3); [Sophia Prater, ORCA introduction](https://medium.com/design-bootcamp/introducing-orca-the-third-diamond-in-your-ux-process-23a1babb0389); [Prater, requirements example](https://sophiavux.medium.com/prioritizing-prioritization-for-product-designers-91e78a28f62e).

Source status: official publisher overview and public author articles; not full-text review of the Johnson/Henderson book.

## The model deliberately excludes

Colors, viewport layouts, named controls, screen hierarchy, CSS, and animation curves. These come later and are constrained by the conceptual model rather than defining it.

## ORCA prompts, rendered operationally

- **Objects:** Which stable concepts do people talk about? What outcomes do they support?
- **Relationships:** Nested, linked, one-to-many, many-to-many, ordered, optional, or dependent? What is the ownership and deletion semantics?
- **Calls to action:** What can each actor do to each object, when, and why?
- **Attributes:** Required or optional; editable or derived; provenance, permissions, and privacy?

Example: A resource is *linked* to an exploration instead of owned by it. Then deleting the exploration should not necessarily delete the resource. That relationship rule is much more consequential than the visual representation.

## Audit for conceptual leaks

- Two labels for the same thing?
- One label with multiple conflicting meanings?
- An object that is only ever a child of an implementation feature?
- Missing state changes or contradictions between operations?
- Important user action that doesn't have an object it acts on?
