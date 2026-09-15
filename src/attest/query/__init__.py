"""C8 — Query agent: natural-language questions answered over the *verified*
store only, via text-to-SQL against a read-only view that excludes
unvalidated low-confidence fields.

in  -> natural-language question
out -> answer + the SQL it ran (always surfaced, for auditability)
tech -> LangGraph, Qwen3-8B, SQLAlchemy

See docs/ARCHITECTURE.md#c8--query-agent.
"""
