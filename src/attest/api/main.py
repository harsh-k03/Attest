"""FastAPI application entrypoint.

TODO(week 5): wire ingest -> router -> extract -> validate -> (commit |
agent.graph) as an async pipeline behind POST /documents, with GET
/documents/{id} for status and /review/* for the C7 queue. See
docker-compose.yml for the intended service topology.
"""

from fastapi import FastAPI

app = FastAPI(title="Attest", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}
