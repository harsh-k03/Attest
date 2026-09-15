"""LangGraph definition of the repair cycle.

Nodes: extract -> validate -> {commit | diagnose -> strategy -> extract (loop,
max 2 retries) | escalate}. See the Figure 2 diagram in docs/ARCHITECTURE.md §4.

TODO(week 4): build with langgraph.graph.StateGraph; attempt counter in the
graph state is what bounds the retry loop (max 2 repairs, i.e. 3 total
extraction attempts including attempt 0).
"""

MAX_REPAIR_ATTEMPTS = 2


def build_graph():
    raise NotImplementedError("C6 agent: build_graph() — see docs/ARCHITECTURE.md §11 Week 4")
