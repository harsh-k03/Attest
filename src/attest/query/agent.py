"""Text-to-SQL agent over the verified-records view.

TODO(week 5): LangGraph agent with a single SQL-execution tool scoped to a
read-only database view/role that only exposes verified, non-escalated
extractions (see docs/ARCHITECTURE.md §3 C8 and §6).
"""


def answer(question: str) -> dict:
    """Return {"answer": str, "sql": str}."""
    raise NotImplementedError("C8 query: answer() — see docs/ARCHITECTURE.md §11 Week 5")
