"""Loads a schema's YAML rule set and evaluates it against an ExtractionRecord.

TODO(week 3): implement rule evaluation for the four categories described in
docs/ARCHITECTURE.md §3 (C5) and §6 (arithmetic/type/cross-field/referential),
producing a report shaped like:

    {"passed": bool, "rules": [{"rule": str, "passed": bool, "fields": [str]}]}
"""

from pathlib import Path

RULES_DIR = Path(__file__).parent / "rules"


def load_rules(schema_id: str) -> dict:
    raise NotImplementedError("C5 validate: load_rules() — see docs/ARCHITECTURE.md §11 Week 3")


def validate(record) -> dict:
    raise NotImplementedError("C5 validate: validate() — see docs/ARCHITECTURE.md §11 Week 3")
