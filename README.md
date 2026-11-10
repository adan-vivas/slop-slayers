# Slop Slayers

**Making AI a better design partner.**

Open-source agent skills that help AI reason, design, and collaborate with humans.

Slop Slayers is a growing collection of practical skills for design agents. Our goal is better judgment—not just faster generation. Each skill provides a repeatable process, references, and ways to critique the result.

## Skills

| Skill | What it helps with | Status |
| --- | --- | --- |
| [Conceptual Interaction Design](skills/conceptual-interaction-design/SKILL.md) | Define domain concepts, actions, relationships, and rules **before** choosing interface components. | v0.1 — experimental |

### Install

Install the first skill using the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add adan-vivas/slop-slayers --skill conceptual-interaction-design
```

To install it globally (on supported agents):

```bash
npx skills add adan-vivas/slop-slayers --skill conceptual-interaction-design -g
```

Alternatively, copy `skills/conceptual-interaction-design/` into your agent's project or personal skills directory. The supported installation path depends on the agent.

### Use

Ask your agent to *use conceptual-interaction-design to define the domain model for my product before creating screens*. The skill will identify concepts, their purposes and states, actions, semantic rules, ambiguities, and alternative interaction models. It is not meant to block straightforward implementation requests.

## How this repository is organized

```text
skills/
  conceptual-interaction-design/
    SKILL.md
    references/
    templates/
evals/
scripts/
ATTRIBUTION.md
LICENSE
```

The `evals/` folder contains paired test cases and a scoring rubric. The tools check packaging and help score human-reviewed outputs; **the skill has not yet been shown to improve design outcomes in controlled evaluations**.

Validate the current package with Python 3.10+:

```bash
python3 scripts/validate.py
```

## Philosophy

- Model what the product **is** before deciding how it **looks**.
- Treat design as reasoning about people, systems, and consequences—not assembly of familiar components.
- Make agent assumptions explicit, keep decisions reversible, and give human designers meaningful control.
- Use research as a tool for better design decisions, not as decorative citations.

## Credits

Inspired by [Maggie Appleton's post](https://x.com/Mappletons/status/2114779610596675824) on getting AI agents to reason about interfaces at the noun, verb, and grammar level. See [ATTRIBUTION.md](ATTRIBUTION.md) for the intellectual foundations and links to the original works.

## License

[MIT](LICENSE) for original repository content. Referenced third-party works retain their own rights.
