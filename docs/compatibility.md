# Compatibility evidence

[Installation](installation.md) · [Documentation map](README.md)

These checks were run on Linux on 2026-10-24 against revision `604fafa`.
Discovery, packaging, and app import are separate checks. Passing one does not
establish the others.

| Environment or operation | Result | Evidence and limit |
| --- | --- | --- |
| Codex CLI 0.163.0 | Project skill invocation exercised | A temporary `.agents/skills/ontolog-interview` copy responded to `$ontolog-interview` with the skill's context-establishment procedure. Ephemeral, read-only session; no interview writes tested in that CLI. |
| Claude Code 2.1.309 | Project skill invocation exercised | A temporary `.claude/skills/ontolog-interview` copy responded to `/ontolog-interview` with the context checklist and reference-read instruction. Tools were disabled, so reference reads and repository writes were not tested. |
| Personal skill directories | Installer behavior tested | Automated tests check destination selection and complete copies. Personal installations were not changed or invoked during this probe. |
| ZIP extraction and independent initialization | Passed | The exported archive contained one complete skill folder; its extracted and installed copies could initialize empty company repositories without the source checkout. |
| Claude web / Cowork ZIP import | Untested | No account UI/import session was available to the evaluator. |
| ChatGPT desktop / Work and other native apps | Untested | No native-app discovery or import session was available. |
| Windows and macOS | Untested | This probe and current CI ran on Linux. |

## Reproduce the CLI discovery probe

Use a disposable project directory and install the complete skill into its
`.agents/skills/ontolog-interview` or `.claude/skills/ontolog-interview` directory
with `ontolog.py install --agent custom --dest PATH`. Use a separate ejected
company repository for any later interview; project skill discovery is not a
place to store company records in the public checkout.

The successful Codex command was:

```sh
codex --ask-for-approval never exec --cd /path/to/disposable-project \
  --sandbox read-only --skip-git-repo-check --ephemeral --ignore-user-config \
  '$ontolog-interview For this synthetic compatibility check, state the first step you would take to begin an interview. Do not inspect or change files.'
```

It responded with the need to establish domain, contributor, audience, and time.
The host also emitted a bubblewrap warning; successful text output does not prove
that file operations would succeed in that sandbox.

From the disposable Claude project, the successful command was:

```sh
claude --print --setting-sources project --tools '' --output-format text \
  '/ontolog-interview For this synthetic compatibility check, state the first step you would take to begin an interview. Do not inspect or change files.'
```

It named `references/interview-method.md` and explicitly said it skipped that read
because the prompt prohibited file inspection. These are one-turn invocation
checks, not full interviews or proof of automatic skill selection.

The probe also passed all 15 setup/documentation tests and exercised `eject`,
custom `install`, `export-skill`, ZIP extraction, and the installed initializer.
Generated company instances had empty records and no inherited Git metadata.
All writes were confined to temporary directories; personal agent settings were
unchanged.

## Native-app verification still needed

For each app/version an evaluator can access:

1. Import the released skill ZIP using that app's supported skill interface.
2. Start a fresh session, invoke the skill, and verify reference access.
3. Use a fictional contributor and a disposable repository or contribution bundle.
4. Download the contribution, inspect its provenance and confirmation status, and
   validate it in the intended company repository.
5. Record the app/version, date, artifact revision, file-access boundary, and any
   manual handoff. Remove the disposable installation afterward if appropriate.

Do not infer successful app import from a valid ZIP or a CLI installation.
Reports should contain synthetic artifacts only, never account credentials or
private company records.
