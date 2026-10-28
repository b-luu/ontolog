#!/usr/bin/env python3
"""Validate a dataset's records/ folder. Does not verify business truth or identity."""

import argparse
from datetime import date
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Install the repository's requirements.txt first.")


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate fields rather than silently replacing earlier evidence."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str):
            raise ValueError("Metadata keys must be strings")
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

STATES = {
    "domain": {"draft", "active", "deprecated"},
    "contributor": {"draft", "active", "deprecated"},
    "source": {"draft", "available", "deprecated"},
    "session": {"draft", "proposed", "confirmed"},
    "concept": {"draft", "proposed", "confirmed", "approved", "disputed", "deprecated"},
    "assertion": {"draft", "proposed", "confirmed", "approved", "disputed", "deprecated"},
    "metric": {"draft", "proposed", "confirmed", "approved", "disputed", "deprecated"},
    "question": {"open", "resolved"},
    "decision": {"proposed", "approved", "rejected"},
}
METRIC_STRINGS = {
    "definition", "business_purpose", "formula", "population", "grain", "identity_rule",
    "unit", "time_window", "time_field", "timezone", "aggregation", "zero_handling",
    "late_data_policy", "rounding", "implementation_ref",
}
STRINGS = {
    "domain": {"definition"}, "contributor": {"role", "team"},
    "source": {"source_kind", "locator"},
    "session": {"purpose", "retention", "resume_point"},
    "concept": {"definition", "concept_kind"},
    "assertion": {"subject_id", "predicate", "evidence_kind"},
    "metric": METRIC_STRINGS,
    "question": {"question_kind", "question"},
    "decision": {"outcome", "rationale"},
}
LISTS = {
    "domain": {"steward_ids"}, "contributor": set(), "source": set(),
    "session": {"participant_ids", "captured_ids"}, "concept": {"aliases"},
    "assertion": set(),
    "metric": {"concept_ids", "inclusions", "exclusions", "dimensions", "worked_examples"},
    "question": {"related_ids", "answer_ids"},
    "decision": {"target_ids", "approver_ids", "approval_source_ids"},
}
COMMON_STRINGS = {"id", "type", "title", "status", "visibility", "created", "updated"}
COMMON_LISTS = {"scope_ids", "contributor_ids", "source_ids", "unknowns"}
OPTIONAL_STRINGS = {"effective_from", "effective_to", "decision_id"}
OPTIONAL_LISTS = {"supersedes_ids", "confirmed_by_ids", "confirmation_source_ids"}
ENUMS = {
    "visibility": {"public", "internal", "restricted"},
    "concept_kind": {"entity", "event", "state", "category", "role", "other"},
    "evidence_kind": {"stated", "inferred", "derived"},
    "source_kind": {"interview", "document", "query", "dashboard", "practice", "other"},
    "retention": {"summary_only", "transcript_authorized", "external_only"},
    "question_kind": {"competency", "clarification", "disagreement", "implementation"},
    "outcome": {"adopt", "defer", "reject"},
}
REFERENCES = {
    "scope_ids": {"domain"}, "contributor_ids": {"contributor"},
    "steward_ids": {"contributor"}, "participant_ids": {"contributor"},
    "approver_ids": {"contributor"}, "confirmed_by_ids": {"contributor"},
    "source_ids": {"source", "session"},
    "confirmation_source_ids": {"source", "session"},
    "approval_source_ids": {"source", "session"}, "decision_id": {"decision"},
    "concept_ids": {"concept"}, "captured_ids": {"concept", "assertion", "metric", "question"},
    "target_ids": {"concept", "assertion", "metric"},
    "related_ids": set(STATES), "answer_ids": set(STATES),
    "subject_id": set(STATES), "object_id": set(STATES),
    "supersedes_ids": set(STATES),
}


def parse_record(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)(.*)\Z", text, re.S)
    if not match:
        raise ValueError("Missing YAML front matter")
    try:
        record = yaml.load(match.group(1), Loader=UniqueLoader)
    except RecursionError as exc:
        raise ValueError("YAML nesting exceeds the parser's supported depth") from exc
    if not isinstance(record, dict):
        raise ValueError("Front matter must be a mapping")
    if not match.group(2).strip():
        raise ValueError("Record body must contain its explanation/evidence")
    return record


def validate(root):
    root = Path(root)
    errors, records = [], {}
    record_root = root / "records"
    if not record_root.is_dir():
        return [f"{root}: records/ directory does not exist"], 0

    for path in sorted(record_root.rglob("*.md")):
        def fail(message):
            errors.append(f"{path.relative_to(root)}: {message}")

        try:
            r = parse_record(path)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            fail(str(exc))
            continue
        kind = r.get("type")
        if not isinstance(kind, str) or kind not in STATES:
            fail("Unknown or missing record type")
            continue
        before = len(errors)
        strings = COMMON_STRINGS | STRINGS[kind]
        lists = COMMON_LISTS | LISTS[kind]
        allowed = strings | lists | OPTIONAL_STRINGS | OPTIONAL_LISTS | {"schema_version"}
        if kind == "assertion":
            allowed |= {"object_id", "value"}
        for field in r:
            if field not in allowed and not field.startswith("x_"):
                fail(f"Unknown field {field}; use x_ for documented extensions")
        if type(r.get("schema_version")) is not int or r["schema_version"] != 1:
            fail("schema_version must be integer 1")
        for field in strings | (OPTIONAL_STRINGS & r.keys()):
            v = r.get(field)
            allow_empty = kind == "metric" and field in METRIC_STRINGS - {"definition", "business_purpose"}
            if not isinstance(v, str) or (not v.strip() and not allow_empty):
                fail(f"{field} must be a {'possibly empty' if allow_empty else 'nonempty'} string")
        for field in lists | (OPTIONAL_LISTS & r.keys()):
            v = r.get(field)
            if not isinstance(v, list) or any(not isinstance(x, str) or not x.strip() for x in v):
                fail(f"{field} must be a list of nonempty strings")
            elif len(v) != len(set(v)):
                fail(f"{field} contains duplicate values")
        for field, value in r.items():
            items = value if isinstance(value, list) else [value]
            if any(isinstance(x, (dict, list)) for x in items):
                fail(f"{field} must be flat scalar/list metadata")
            if field in ENUMS and (not isinstance(value, str) or value not in ENUMS[field]):
                fail(f"Invalid {field}")
        if not isinstance(r.get("status"), str) or r["status"] not in STATES[kind]:
            fail(f"Invalid lifecycle status for {kind}")
        rid = r.get("id", "")
        if not isinstance(rid, str) or not re.fullmatch(rf"{kind}-[a-z0-9]+(?:-[a-z0-9]+)*", rid):
            fail("ID must be lowercase and prefixed with its record type")
        if isinstance(rid, str) and rid in records:
            fail(f"Duplicate ID {rid}")
        for field in ("created", "updated", "effective_from", "effective_to"):
            if field not in r:
                continue
            try:
                if not isinstance(r[field], str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r[field]):
                    raise ValueError()
                date.fromisoformat(r[field])
            except ValueError:
                fail(f"{field} must be a quoted ISO date YYYY-MM-DD")
        if kind == "assertion":
            targets = [f for f in ("object_id", "value") if f in r]
            if len(targets) != 1 or not isinstance(r.get(targets[0]) if targets else None, str) or not r.get(targets[0], "").strip():
                fail("Assertion needs exactly one nonempty object_id or value")
        if len(errors) == before:
            records[rid] = (r, path)

    # Shape-checked records can now be inspected without exceptions on malformed fields.
    for rid, (r, path) in records.items():
        def fail(message):
            errors.append(f"{path.relative_to(root)}: {message}")

        kind = r["type"]
        if r["updated"] < r["created"]:
            fail("updated precedes created")
        if r.get("effective_to") and r.get("effective_from") and r["effective_to"] <= r["effective_from"]:
            fail("effective_to must be after effective_from (exclusive end)")
        if kind != "contributor" and not r["scope_ids"]:
            fail("scope_ids must identify at least one domain")
        if kind not in {"domain", "contributor"} and not r["contributor_ids"]:
            fail("contributor_ids must identify an attributed contributor")
        if kind not in {"domain", "contributor", "source"} and not r["source_ids"]:
            fail("source_ids must identify evidence")
        if kind == "domain" and r["scope_ids"] != [rid]:
            fail("A domain must be scoped to itself only")
        for field, target_types in REFERENCES.items():
            if field not in r:
                continue
            refs = r[field] if isinstance(r[field], list) else [r[field]]
            for ref in refs:
                if ref == rid and not (kind == "domain" and field == "scope_ids"):
                    fail(f"{field} cannot reference the record itself")
                target = records.get(ref)
                if target is None:
                    fail(f"{field}: missing or invalid target {ref}")
                elif target[0]["type"] not in target_types:
                    fail(f"{field}: wrong target type for {ref}")
                elif field == "supersedes_ids" and target[0]["type"] != kind:
                    fail("supersedes_ids must reference the same record type")
        if r["status"] == "confirmed":
            for field in ("confirmed_by_ids", "confirmation_source_ids"):
                if not r.get(field):
                    fail(f"Confirmed record needs {field}")
        if kind == "session" and not r["participant_ids"]:
            fail("Session needs participants")
        if kind == "question" and r["status"] == "resolved" and not r["answer_ids"]:
            fail("Resolved question needs answer_ids")
        if kind == "decision":
            if not r["target_ids"]:
                fail("Decision needs target_ids")
            if r["status"] == "approved":
                for field in ("approver_ids", "approval_source_ids", "effective_from"):
                    if not r.get(field):
                        fail(f"Approved decision needs {field}")
                for scope in r["scope_ids"]:
                    domain = records.get(scope)
                    if domain and domain[0]["type"] == "domain" and not set(domain[0]["steward_ids"]) & set(r["approver_ids"]):
                        fail(f"No configured steward approved decision scope {scope}")
        if kind in {"concept", "assertion", "metric"} and r["status"] == "approved":
            if r["unknowns"]:
                fail("Approved definition cannot have unresolved unknowns")
            decision = records.get(r.get("decision_id"))
            d = decision[0] if decision else {}
            if d.get("type") != "decision" or d.get("status") != "approved" or d.get("outcome") != "adopt":
                fail("Approved definition needs an approved adoption decision")
            elif rid not in d["target_ids"] or not set(r["scope_ids"]) <= set(d["scope_ids"]):
                fail("Adoption decision must cover this record and all its scopes")
            elif d.get("effective_from"):
                # Omitted definition bounds inherit the adopting decision's bounds.
                start = r.get("effective_from", d["effective_from"])
                end = r.get("effective_to", d.get("effective_to"))
                if (start < d["effective_from"]
                        or (d.get("effective_to") and (end is None or end > d["effective_to"]))
                        or (end is not None and end <= start)):
                    fail("Adoption decision must cover this record's effective period (exclusive end)")
            if kind == "assertion" and r["evidence_kind"] == "inferred":
                fail("Unchecked inferred assertion cannot be approved")
            if kind == "metric":
                for field in METRIC_STRINGS:
                    if not r[field].strip():
                        fail(f"Approved metric needs {field}")
                for field in ("concept_ids", "inclusions"):
                    if not r[field]:
                        fail(f"Approved metric needs {field}")
                if len(r["worked_examples"]) < 3:
                    fail("Approved metric needs at least three worked examples")
        if kind == "metric" and r["status"] != "approved":
            empty = sorted(f for f in METRIC_STRINGS if not r[f].strip())
            if empty and not r["unknowns"]:
                fail("Incomplete metric must describe unsettled parameters in unknowns")

    return errors, len(records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    errors, count = validate(args.repository)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"Validation failed: {len(errors)} issue(s).", file=sys.stderr)
        return 1
    print(f"Valid structure: {count} records. Business truth and approval identity require human review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
