"""Post-generation hook: create symlinks matching the lawwu/skills conventions."""

import os
import shutil

PLUGIN_NAME = "{{ cookiecutter.plugin_name }}"


def make_symlink(src, dst, fallback_copy=None):
    try:
        os.symlink(src, dst)
        print(f"Created symlink: {dst} -> {src}")
    except OSError:
        if fallback_copy:
            shutil.copy2(fallback_copy, dst)
            print(f"Created copy: {dst} (symlink not supported on this platform)")
        else:
            print(f"Warning: could not create symlink {dst} -> {src}")


# CLAUDE.md -> AGENTS.md
make_symlink("AGENTS.md", "CLAUDE.md", fallback_copy="AGENTS.md")

# .agents/skills -> ../plugins/<plugin_name>/skills  (mirrors skills.sh ecosystem layout)
os.makedirs(".agents", exist_ok=True)
make_symlink(f"../plugins/{PLUGIN_NAME}/skills", ".agents/skills")
