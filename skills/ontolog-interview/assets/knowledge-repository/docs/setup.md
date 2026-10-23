# Set up an organizational repository

[Repository guide](../README.md) · [Record templates](../templates/README.md) · [Field guide](model.md)

## Create your own instance first

Run the kit's initializer with an absolute destination outside its checkout, or download/copy only this template into your own separate directory. The initializer refuses a destination within the public kit, and an existing destination is never overwritten. The bundled template is reusable scaffolding: leave it empty of company knowledge.

A generated instance has no inherited `.git` directory, history, or remote. It is a local folder; it has no hosted privacy setting. If using Git, initialize its own history, create a separate **private** repository on your chosen host, verify its collaborators and visibility, and add that private remote. Do not use a fork of the public kit as your company's knowledge repository. Its open-source status does not determine the visibility of a new repository you create.

Contributors work on branches/copies of the organization's private instance. Share it only with its intended audience. Local filesystem access, backups, and the systems used by agents also need to match that audience. `visibility` metadata does not restrict access.

Send reusable improvements upstream separately, using synthetic examples and template/tooling changes. Private company records stay in the private instance. To upgrade, review and apply template/schema changes to your own repository; do not replace your records or re-run initialization over them.

## Establish scope and start interviewing

1. Choose one bounded domain and the decisions it should support. Establish the repository's audience, content rights, and sharing boundary.
2. Create a contributor note for the person coordinating the pilot. A pseudonym or organizational identifier is sufficient; avoid unnecessary personal information.
3. Create a domain from the template, including in-scope/out-of-scope statements and initial competency questions as question records.
4. Have an authorized human establish `steward_ids` for the domain. Leave this list empty while ownership is unknown. Repository validation does not verify this person's real-world authority.
5. Give contributors their own working copies/branches and the interview skill. Start with independent accounts of the same practical workflow, plus people from adjacent roles.
6. Review one small contribution at a time. Use an explicit adoption decision before changing proposed definitions to approved. A merged contribution may remain proposed or disputed.
7. Pilot the questions and worked metric examples with contributors; adjust the method and schema from actual failures.

The template has no company-specific policy, steward, or approved definition. A successful first session can end with entirely proposed records, explicit uncertainty, and a clear next question.

Continue with [collaboration](collaboration.md) for review and approval, and [scope boundaries](boundaries.md) for the relationship to existing analytical definitions.

To use without Git, exchange contribution folders containing new records and referenced sources that can be shared. Have one coordinator import into the canonical repository after ID/reference validation. Use an agreed editing lock for shared files. Do not let file-sync software silently resolve competing edits to approved definitions.
