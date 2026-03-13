# Agent Instructions

## Skill Structure
```
plugins/{{ cookiecutter.plugin_name }}/skills/<skill-name>/SKILL.md
```

## Creating/Updating Skills

### Registration Checklist
1. Create `plugins/{{ cookiecutter.plugin_name }}/skills/<skill-name>/SKILL.md`
2. Add to `README.md` Available Skills table (alphabetical by canonical skill name; exclude aliases/symlinks)
3. Add to `.claude/settings.json`: `Skill({{ cookiecutter.plugin_name }}:<skill-name>)`

## Key Conventions
- Frontmatter `---` must be the **first line** of SKILL.md — no comments before it
- `name` field must match the directory name exactly
- `description` includes trigger keywords — this is how agents discover the skill
- Attribution comments go **after** the closing `---`
- Python scripts: always use `uv run <script>`, never `python` or `python3`
- Keep SKILL.md under 500 lines; move reference material to `references/`

## References
- Skill template and optional fields: `README.md`
- Testing and PR workflow: `CONTRIBUTING.md`
- [Agent Skills Spec](https://agentskills.io/specification)
