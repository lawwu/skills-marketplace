# Contributing

## Philosophy

This repository favors **incremental change** over perfection. Skills are living documents that improve over time through small, iterative updates.

- **Bias toward action** - Ship small improvements rather than waiting for the perfect solution
- **Self-review is the default** - You know your changes best
- **Iterate freely** - Don't hesitate to refine existing skills

## Local Setup

```bash
git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git ~/{{ cookiecutter.repo_name }}
cd ~/{{ cookiecutter.repo_name }}
```

Install [prek](https://github.com/j178/prek) to run pre-commit checks locally (mirrors the CI `prek` workflow):

```bash
pip install prek
prek  # run all checks
```

Optionally install pre-commit hooks so checks run automatically on every commit:

```bash
pip install pre-commit
pre-commit install
```

## Repository Structure

```
{{ cookiecutter.repo_name }}/
├── .claude-plugin/
│   └── marketplace.json      # Marketplace manifest
├── plugins/
│   └── {{ cookiecutter.plugin_name }}/
│       ├── .claude-plugin/
│       │   └── plugin.json   # Plugin manifest
│       ├── agents/           # Reusable subagents
│       └── skills/           # Add skill directories here
├── AGENTS.md                 # Agent-facing documentation
├── CLAUDE.md                 # Symlink to AGENTS.md
└── README.md
```

## Adding a New Skill

1. Create `plugins/{{ cookiecutter.plugin_name }}/skills/<skill-name>/SKILL.md`

2. Add required YAML frontmatter:

   ```yaml
   ---
   name: skill-name
   description: What this skill does. Include trigger keywords.
   ---
   ```

3. Update `README.md` to add the skill to the Available Skills table in alphabetical order by skill name

4. Add the skill to `.claude/settings.json`:

   ```json
   "Skill({{ cookiecutter.plugin_name }}:skill-name)"
   ```

### Skill Template

```yaml
---
name: my-skill
description: A clear description of what this skill does and when to use it. Include keywords that help agents identify when this skill is relevant.
---

# My Skill Name

## Instructions

Step-by-step guidance for the agent.

## Examples

Concrete examples showing expected input/output.

## Guidelines

- Specific rules to follow
- Edge cases to handle
```

### Naming Conventions

- **name**: 1-64 characters, lowercase alphanumeric with hyphens only
- **description**: Up to 1024 characters, include trigger keywords
- Keep SKILL.md under 500 lines; split longer content into reference files

### Optional Fields

| Field | Description |
|-------|-------------|
| `license` | License name or path to license file |
| `compatibility` | Environment requirements (max 500 chars) |
| `allowed-tools` | Comma-separated list of tools the skill can use |
| `metadata` | Arbitrary key-value pairs for additional properties |

```yaml
---
name: my-skill
description: What this skill does
license: MIT
allowed-tools: Read, Grep, Glob
---
```

### Vendoring Skills

When vendoring a skill from an external source, retain proper attribution:

1. Add a comment at the top of the file (after the closing `---`) referencing the original source:
   ```markdown
   <!--
   Based on [Original Name] by [Author/Org]:
   https://github.com/example/original-source
   -->
   ```

2. Include a `LICENSE.txt` in the skill directory if the original has specific licensing requirements.

## Testing Skills

Before merging, test your changes locally:

1. **Install the plugin from your local clone**

   ```bash
   claude plugin marketplace add ~/{{ cookiecutter.repo_name }}
   claude plugin install {{ cookiecutter.plugin_name }}
   ```

2. **Restart Claude Code** to pick up changes

3. **Invoke the skill** in a relevant context

   ```bash
   # For explicit invocation
   /skill-name

   # Or describe a task that should trigger the skill
   ```

4. **Verify behavior** - Check that the skill produces the expected guidance and handles edge cases appropriately

## Pull Request Workflow

All changes go through the PR flow, but formal review is optional.

- **Self-review and merge** when you're confident in your change
- **Request review** only when you want a second pair of eyes
- Keep PRs focused - one skill or one improvement per PR when practical
