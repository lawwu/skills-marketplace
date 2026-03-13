# Skills Marketplace

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating an agent skills marketplace compatible with [Claude Code](https://code.claude.com), the [Agent Skills specification](https://agentskills.io/specification), and [skills.sh](https://skills.sh).

## Some Best Practices

- Symbolic links
   - `CLAUDE.md` -> `AGENTS.md`
   - `.agents/skills` -> `../plugins/my-skills/skills`
- Github Actions
   - [Claude Review]({{cookiecutter.repo_name}}/.github/workflows/claude.yml)
   - [Skill Review]({{cookiecutter.repo_name}}/.github/workflows/skill-review.yml)
   - [Validate-Frontmatter]({{cookiecutter.repo_name}}/.github/workflows/validate-frontmatter.yml)

## Usage

```bash
# Install cookiecutter if you haven't already
pip install cookiecutter

# Generate a new skills marketplace
cookiecutter gh:{{ cookiecutter_repo_placeholder }}/skills-marketplace
# or from local clone:
cookiecutter path/to/skills-marketplace
```

You will be prompted for:

| Variable | Description | Default |
|----------|-------------|---------|
| `repo_name` | Repository / directory name | `my-skills` |
| `plugin_name` | Plugin name (used in manifests and install commands) | same as `repo_name` |
| `plugin_description` | Short description of the plugin | |
| `author_name` | Your full name | |
| `github_username` | Your GitHub username | |
| `license` | License for the project | `MIT` |

## What Gets Generated

```
<repo_name>/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace manifest
├── .github/
│   ├── CODEOWNERS                # Restricts @claude bot to authorized users
│   ├── scripts/
│   │   └── validate-frontmatter.ts   # Bun script for YAML frontmatter validation
│   └── workflows/
│       ├── claude.yml            # Triggers Claude Code on @claude mentions
│       ├── skill-review.yml      # Automated AI review of skill PRs
│       └── validate-frontmatter.yml  # CI frontmatter validation
├── plugins/
│   └── <plugin_name>/
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin manifest
│       ├── agents/               # Reusable subagent definitions (.md)
│       └── skills/
│           └── skill-creator/    # Bundled skill for creating/testing skills
├── .gitignore
├── .pre-commit-config.yaml       # trailing-whitespace, YAML, actionlint, ruff
├── AGENTS.md                     # Agent-facing instructions
├── CLAUDE.md -> AGENTS.md        # Symlink (created by post-gen hook)
├── CONTRIBUTING.md               # Development workflow
├── LICENSE                       # Auto-populated for MIT, Apache-2.0, Unlicense
├── README.md                     # Installation & skill inventory
└── pyproject.toml                # Ruff configuration (for skill scripts)
```

## Post-Generation Steps

1. **Add your GitHub secret** `ANTHROPIC_API_KEY` in repo Settings → Secrets → Actions
3. **Install locally** to test:
   ```bash
   claude plugin marketplace add ~/path/to/<repo_name>
   claude plugin install <plugin_name>
   ```
4. **Push to GitHub** and install from the registry:
   ```bash
   claude plugin marketplace add <github_username>/<repo_name>
   claude plugin install <plugin_name>@<plugin_name>
   ```

## Contributing

Install [prek](https://github.com/getsentry/prek) for pre-commit linting:

```bash
pip install prek
pre-commit install
```


## Inspired By

- [lawwu/skills](https://github.com/lawwu/skills)
- [Sentry's skills marketplace](https://github.com/getsentry/skills)
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

## License

MIT
