"""C6 — Repair agent: a LangGraph cyclic graph implementing the repair loop.

On validation failure it diagnoses which fields are implicated, chooses a
repair strategy, re-runs a narrowed extraction, and re-validates. Bounded at
two attempts before escalating to the human review queue (C7).

in  -> failed record + validation report
out -> repaired record, or escalation
tech -> LangGraph, Qwen3 via Ollama, tool-calling

See docs/ARCHITECTURE.md#4-the-repair-loop for the full state diagram and the
failure -> strategy mapping.
"""
