# Attest

**A document extraction system that knows when it is wrong.**

Attest turns invoices and receipts into structured, trustworthy data. Any modern
vision-language model will return plausible JSON for a document — the problem is
that it does so whether or not the JSON is correct. Attest treats extraction as
only the first of four stages: extract → estimate confidence → validate
deterministically → repair or escalate. The output is never just a JSON object;
it is a JSON object plus a defensible, auditable claim about which fields can be
trusted.

> Status: **pre-implementation** (architecture v0.1, drafted 12 Sept 2026).
> This repository currently holds the design and the scaffolding described
> below — see [Build milestones](#build-milestones) for what's shipped vs. planned.

Full design rationale, diagrams, and decision log: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Design goals

- **Calibrated, not just accurate.** Every extracted field carries a confidence
  score whose stated probability matches its observed correctness rate.
- **Deterministic checks over probabilistic ones.** Arithmetic and cross-field
  consistency are verified by code, never by asking a model to check itself.
- **Recover before escalating.** A failed validation triggers a bounded repair
  attempt before consuming a human's attention.
- **Auditable.** Every field records which component produced it, on which
  attempt, and why it was accepted.
- **Permissively licensed end to end.** No component blocks commercial deployment.

**Non-goals (v1):** general-purpose OCR, handwriting / severely degraded scans,
non-English documents, contracts (v2).

## How it works

```
Ingest → Router → Extractor → Validator → Store
                       ↑           │
                       └─ Repair ←─┘ (≤ 2 retries, then → human review queue)
```

A document is rasterized, classified, and passed to a fine-tuned
vision-language extractor. A deterministic rule engine checks the result
(arithmetic, formats, cross-field consistency, vendor lookups). Passing
records are committed; failing ones enter a repair loop — an agent diagnoses
which fields are implicated, picks a repair strategy (re-crop, targeted
re-prompt, or OCR fallback), and re-validates — bounded at two attempts before
escalating to a human reviewer. Corrections feed back as training labels.
A text-to-SQL agent answers questions over the verified store only.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the full pipeline and
repair-loop diagrams, the component-by-component specification (C1–C8), the
data model, and the escalation policy.

## Repository layout

```
attest/
├── README.md              ← you are here
├── docs/ARCHITECTURE.md   ← full architecture spec, diagrams, data model, eval plan
├── docker-compose.yml     ← api + mysql + ollama, one command up
├── src/attest/
│   ├── ingest/            C1 — rasterise, deskew, normalise
│   ├── router/            C2 — document type classifier
│   ├── extract/           C3 — model wrapper, prompts, guided decoding
│   ├── confidence/        C4 — logprob aggregation + calibrator
│   ├── validate/          C5 — rule engine + YAML rule sets
│   ├── agent/              C6 — LangGraph repair cycle
│   ├── store/             models, migrations, queries
│   ├── query/             C8 — text-to-SQL agent
│   └── api/               FastAPI routes
├── training/              prepare_cord.py, train_lora.py, calibrate.py
├── eval/                  run_benchmark.py, metrics.py, results/ (committed)
├── ui/                    C7 — Gradio review queue
├── tests/
└── notebooks/             exploration only, never the source of truth
```

## Technology stack

| Layer | Choice | Licence |
|---|---|---|
| Extractor | Qwen2.5-VL-3B-Instruct + LoRA | Apache-2.0 |
| OCR fallback | PaddleOCR-VL (0.9B) | Apache-2.0 |
| Agent LLM | Qwen3 (4B dev / 8B eval) | Apache-2.0 |
| Orchestration | LangGraph | MIT |
| Serving | vLLM + FastAPI | Apache-2.0 |
| Store | MySQL 8 | GPL / dual |
| UI | Gradio | Apache-2.0 |
| Training | PEFT, TRL, bitsandbytes | Apache-2.0 |
| Tracking | Weights & Biases | free tier |

LayoutLMv3 was deliberately excluded despite being an obvious choice — its
weights are CC BY-NC-SA 4.0 (non-commercial), which conflicts with the goal of
a deployable system.

## Datasets

Trained on **CORD-v2** only; evaluated on CORD-v2, **DocILE**, **SROIE**, and
**FUNSD** — the latter three held out entirely to demonstrate generalisation
rather than memorisation. See [`docs/ARCHITECTURE.md#datasets`](docs/ARCHITECTURE.md#7-datasets)
for sources and access notes.

## Evaluation

Four systems compared identically: OCR+rules baseline, zero-shot VLM,
fine-tuned VLM without the agent layer, and the full Attest system. Headline
metrics are field-level F1, document accuracy, expected calibration error, and
automation rate at a fixed precision target (99%). The with/without-repair-loop
ablation is the key evidence that the agentic layer earns its place. Results
land in [`eval/results/`](eval/results) as they're produced.

## Build milestones

| Week | Focus | Gate |
|---|---|---|
| 1 | Data & measurement | Baseline numbers exist and are reproducible from one command |
| 2 | The extractor | Fine-tuned model beats zero-shot baseline on field F1, margin quantified |
| 3 | Trust layer | Calibration error < 0.05; escalation threshold chosen from the precision–coverage curve |
| 4 | The agent | LangGraph repair cycle live; escalation rate measurably lower with it enabled |
| 5 | Ship it | `docker compose up` takes a stranger from clone to a processed document |

## Getting started

```bash
git clone <this-repo>
cd attest
docker compose up
```

(Service wiring lands in Week 5 — see milestones above. Until then, component
modules under `src/attest/` are being built out individually; each has a
docstring describing its contract.)

## License

Code in this repository is MIT licensed (see [`LICENSE`](LICENSE)). Individual
model weights and third-party components retain their own licenses — see the
technology stack table above.
