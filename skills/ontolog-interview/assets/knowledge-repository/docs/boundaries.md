# Business context, analytical definitions, and methods

[Repository guide](../README.md) · [Metric fields](model.md#metric) · [Review procedure](collaboration.md)

The knowledge repository records business meaning, attributed perspectives, evidence, decisions, and unanswered questions. It can also record company-specific interpretation caveats using sourced assertions, such as a policy change that limits comparability. A reported intuition remains proposed until supported and reviewed.

An existing semantic layer or governed model is canonical for executable metric logic. Use `implementation_ref` to identify its metric/model and version. The required `formula` field can describe that calculation with a reference; any copied formula must identify its source revision. Review for agreement rather than keeping two independently edited definitions. There is no automatic synchronization. Capture mismatches as implementation questions and proposed changes.

Deployed code establishes the current calculation; approved business intent establishes what it should mean. Existing code can be wrong. Review discrepancies against the evidence and approved rule, then propose the appropriate correction rather than automatically treating either a new interview claim or the current implementation as correct.

General methods such as validating join grain, avoiding denominator mistakes, or investigating cohort maturity belong in a companion analytical skill/playbook. Warehouse-specific practices such as approved join paths and snapshot caveats can remain with data/model documentation and be linked as sources here. This repository has no dedicated operational-practice schema or query-execution workflow in version 1.

The interviewing skill supports this business knowledge process. A future analytics agent can consume the knowledge, methodological skills, and executable metrics together. A business knowledge repository is also useful outside analytics, including customer support and operational workflows.
