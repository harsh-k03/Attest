"""Attest: a document extraction system that knows when it is wrong.

See docs/ARCHITECTURE.md for the full design. Package layout mirrors the
eight components (C1-C8) described there:

    ingest      C1  rasterise, deskew, normalise
    router      C2  document type classifier
    extract     C3  extractor model wrapper, prompts, guided decoding
    confidence  C4  logprob aggregation + calibrator
    validate    C5  deterministic rule engine
    agent       C6  LangGraph repair cycle
    store       --  ExtractionRecord persistence (models, queries)
    query       C8  text-to-SQL agent over the verified store
    api         --  FastAPI routes
"""

__version__ = "0.1.0"
