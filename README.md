# GCSA Visual System

An Agent Skill for designing, implementing, and reviewing GCSA-branded websites, product consoles, mobile interfaces, diagrams, and campaign assets.

It provides:

- GCSA brand foundations and visual decision priorities
- Marketing, console, mobile, and brand-asset guidance
- Design, review, refactor, and component workflows
- Portable examples and acceptance criteria
- A dependency-free recommendation CLI for generating product-specific visual directions

## Install

Install interactively:

```bash
npx skills add kimi-frontEndEngineer/gcsa-visual-system
```

Install globally for Codex:

```bash
npx skills add kimi-frontEndEngineer/gcsa-visual-system -g -a codex
```

List the skills detected in the repository without installing:

```bash
npx skills add kimi-frontEndEngineer/gcsa-visual-system --list
```

## Use

Ask your agent to use `gcsa-visual-system`, or make a request involving GCSA visual design, UI implementation, design-system decisions, or brand review.

Generate a portable visual-direction brief from the included catalog:

```bash
python3 scripts/recommend.py \
  --surface marketing \
  --task design \
  --product "AI gateway zero trust"
```

Supported surfaces:

- `marketing`
- `console`
- `mobile`
- `asset`

Supported tasks:

- `design`
- `review`
- `refactor`
- `component`

Use `--format json` for machine-readable output.

## Repository contents

```text
SKILL.md               Skill entry point
examples.md            Complete design and review examples
reference.md           Token baselines and delivery checklists
data/catalog.json      Product signals and recommendation data
scripts/recommend.py   Dependency-free recommendation CLI
```

## License and trademarks

The Skill instructions and source code are available under the MIT License.

GCSA names, logos, trademarks, and brand assets are the property of their respective owners and are not licensed under the MIT License. This repository does not grant permission to use GCSA trademarks or imply endorsement.

## Contributing

Keep the Skill portable:

- Do not add machine-specific or organization-internal paths.
- Do not add credentials, private URLs, or proprietary product data.
- Prefer semantic design rules over framework-specific implementation details.
- Validate all four surfaces and task modes after changing the recommendation catalog or script.
