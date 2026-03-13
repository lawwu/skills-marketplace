# {{ cookiecutter.plugin_name }}

{{ cookiecutter.plugin_description }}

Agent skills for Claude Code and other coding agents following the [Agent Skills](https://agentskills.io) open format.

## Installation

### Claude Code

```bash
claude plugin marketplace add {{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
claude plugin install {{ cookiecutter.plugin_name }}@{{ cookiecutter.plugin_name }}
```

Restart Claude Code after installation. Skills activate automatically when relevant.

**Update:**

```bash
claude plugin marketplace update
claude plugin update {{ cookiecutter.plugin_name }}@{{ cookiecutter.plugin_name }}
```

Or run `/plugin` to open the plugin manager.

### Skills Package (skills.sh)

For agents supporting the [skills.sh](https://skills.sh) ecosystem:

```bash
npx skills add {{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}
```

## Available Skills

| Skill | Description |
|-------|-------------|
| [skill-creator](plugins/{{ cookiecutter.plugin_name }}/skills/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance |

## Available Subagents

| Subagent | Description |
|----------|-------------|
| *(none yet — add agents to `plugins/{{ cookiecutter.plugin_name }}/agents/`)* | |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for local setup (including prek), repository structure, skill authoring guidelines, and the PR workflow.

## References

- [Claude Skills](https://code.claude.com/docs/en/skills)
- [Claude Plugins](https://code.claude.com/docs/en/plugins)
- [Agent Skills Specification](https://agentskills.io/specification)

## License

{{ cookiecutter.license }}
