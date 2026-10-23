# Set up Ontolog

[Documentation map](README.md) · [Project structure](project-structure.md)

Requires Python 3.10+ for setup commands; they use only the standard library. Repository validation additionally uses the ejected repository's `requirements.txt`.

## 1. Eject your organization's repository

From the downloaded/cloned Ontolog project:

```sh
python3 ontolog.py eject ../my-company-knowledge
```

This copies the reusable template to a new directory outside the public checkout. Its `records/` folders are empty. It carries its own docs, record templates, license notice, and validator, with no dependence on this checkout, Git history, remote, or automatic upload. The command refuses an existing destination and paths inside the public project, including aliases through symlinks.

Create a separate private Git repository if using hosting, verify the visibility and collaborators, and add only that private remote. Give your agents access to this instance. Keep organizational knowledge out of the public Ontolog checkout and its forks.

Examples require no cleanup. They stay in the public bundle as reference material and are omitted from an ordinary ejection. To include a separate demonstration dataset:

```sh
python3 ontolog.py eject ../ontolog-demo --with-example
```

The fictional records live under `examples/subscription-business/records/`, while the organization's `records/` remains empty. Validate them separately using the example path. Do not rename the sample people and treat the example as an organization's model.

Before ejecting, you can browse the [template guide](../skills/ontolog-interview/assets/knowledge-repository/README.md), [record patterns](../skills/ontolog-interview/assets/knowledge-repository/templates/README.md), and [example walkthrough](../skills/ontolog-interview/assets/knowledge-repository/examples/subscription-business/README.md).

## 2. Install the interview skill

For an interactive menu:

```sh
python3 ontolog.py install
```

For explicit, non-interactive installation:

```sh
python3 ontolog.py install --agent codex
python3 ontolog.py install --agent claude-code
```

Codex uses `~/.agents/skills/ontolog-interview/`; Claude Code uses `~/.claude/skills/ontolog-interview/`. The installer copies the complete skill, including the references and bundled template its instructions use. It refuses to overwrite an existing skill. It does not modify agent configuration or add a remote.

For a harness/version with another discovery path, provide the exact folder:

```sh
python3 ontolog.py install --agent custom --dest /your/skills/ontolog-interview
```

The final directory must be named `ontolog-interview`. Use this override for an existing Codex setup that discovers `~/.codex/skills` instead of the path in the current documentation. Avoid installing the same skill in multiple discovery locations.

## Native apps and hosted environments

The important distinction is where the agent executes and how it discovers skills. A desktop interface may run a local coding session or a hosted session, with different installation and file access behavior.

| Environment | Route | Boundary |
| --- | --- | --- |
| Codex local CLI/IDE/app workspace | Local installation into the environment's skill discovery path | The app must see that filesystem and discover the skill |
| ChatGPT desktop / Work | Standalone skills are documented; use its Skills interface and supported local environment | A local install does not automatically install into every hosted session |
| ChatGPT web/mobile | Official guidance distributes skills through plugins | Ontolog does not yet ship a ChatGPT plugin; generic ZIP upload support is not claimed |
| Claude Code local | `install --agent claude-code` | Personal skills are local to that machine |
| Claude web / Cowork | Export a ZIP and upload through the account's skill settings | Local Claude Code installation alone does not provision Cowork |
| Hosted coding environments | Install in that environment, or use supported project skill discovery | Your laptop's home directory is not automatically shared |
| Other apps | Use their documented import/discovery mechanism | A standard skill folder does not guarantee host support |

To export the complete skill for an app with ZIP import:

```sh
python3 ontolog.py export-skill
```

Output: `dist/ontolog-interview.zip`. The archive contains one `ontolog-interview/` folder with `SKILL.md`, references, scripts, and the bundled template. It contains no Git metadata or company repository. An existing archive is never overwritten. Import it manually into a supported app; exporting is not registration or upload.

For Claude, use Customize > Skills and the upload option. Account/organization settings determine availability. Installing instructions does not grant access to company files, a database, or a Git remote. In an app without persistent repository access, use the interview to produce a contribution bundle, then download and review it into the private repository. That is a manual handoff, not automatic synchronization.

## 3. Start an interview

Point the agent at the private repository and invoke the skill through its host's mechanism. Codex example:

> Use $ontolog-interview to interview me about our customer lifecycle. Our repository is at /absolute/path/to/my-company-knowledge. Capture my perspective before comparing it with existing definitions.

Claude Code uses `/ontolog-interview`; other app selectors differ. If local changes are not detected, refresh skills or start a new session.

Continue with [domain setup](../skills/ontolog-interview/assets/knowledge-repository/docs/setup.md) and the [interview method](../skills/ontolog-interview/references/interview-method.md). Use the [collaboration procedure](../skills/ontolog-interview/assets/knowledge-repository/docs/collaboration.md) to review contributions, then [pilot scenarios](pilot-scenarios.md) to evaluate the method.

## Updates and verification

Keep your company instance independently versioned. Review template/schema updates as migrations rather than ejecting over existing records. For skill updates, inspect the new package and intentionally replace or back up your prior installation; there is no destructive force-install switch.

These scripts have automated filesystem/packaging checks. They have not been tested by importing into each vendor app. A clean public source bundle is assumed: checks reject populated template records and symlinks, but cannot identify confidential prose someone manually inserted elsewhere in a skill.

Vendor instructions checked 2026-10-19:

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills), including local Codex discovery and app/plugin distribution.
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills), including local, Cowork, and cloud boundaries.
- [Claude: Use skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude), including ZIP import.
