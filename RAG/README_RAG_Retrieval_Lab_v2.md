# RAG Retrieval Lab v2 — Real SciFact + HyDE + CRAG-inspired Correction

A concise, reproducible Jupyter notebook: **BM25 → Dense → Hybrid RRF → Cross-Encoder → Retrieval Evaluation**, plus a simple API-free **CRAG-inspired** fallback and optional free-tier **Groq HyDE / grounded generation**.

## Quickstart

1. Open `RAG_Retrieval_Lab_v2_RealData.ipynb` in Colab (or Jupyter with Internet access).
2. Run cells from top to bottom. Main pipeline requires **no API keys**. CPU supported; GPU may accelerate local models.
3. To try HyDE and grounded answers, get a Groq API key via https://console.groq.com/keys ; store as Colab Secret `GROQ_API_KEY`, then set `RUN_API_DEMOS = True` in the optional section.
4. Never commit a key. Free-tier quotas/model availability change. Only public corpus content is sent to Groq.

## Data and evaluation

- Dataset: https://huggingface.co/datasets/Hyukkyu/beir-scifact (BEIR SciFact: 5,183 science abstracts, test queries, relevance judgments; **CC BY-NC 4.0**). Data loaded at runtime; **not** redistributed in this repository.
- Search is against the full corpus; test queries are a reproducible random subset selected with `SEED=42`.
- Metrics: **Recall@5, MRR@5, nDCG@10** using actual SciFact qrels, not synthetic labels.
- The evaluation table displays the results of *your* run; this repository does not claim predetermined benchmark improvements.

## Methods

| Section | Local / no API? | Core idea |
|---|---|---|
| BM25 | Yes | Exact lexical matching |
| SentenceTransformer Dense | Yes | One sentence embedding per real document |
| RRF | Yes | Rank-based BM25 + Dense fusion |
| Cross-Encoder Reranker | Yes | Joint query-document scoring |
| CRAG-inspired correction | Yes | Relevance grading → broader search → abstain |
| HyDE | **Groq key optional** | LLM-generated hypothetical passage used only as search query |
| Grounded answer | **Groq key optional** | LLM constrained to cited retrieved abstracts |

## Limitations

- CRAG here is **inspired by**, not a faithful reproduction of the original CRAG paper; no trained evaluator, web search or knowledge refinement.
- Reranker logits passed through sigmoid are **routing heuristics, not calibrated probabilities**; thresholds must be tuned on held-out validation data.
- The corpus contains **abstracts**, not full-text papers. No document chunking or parent retrieval is needed for this dataset.
- Dense search is exact dot-product over NumPy (normalized vectors), not a persistent vector database or ANN index.
- LLM answers must be inspected; retrieved passages are evidence but generated answers can still be wrong.

Sources: https://github.com/beir-cellar/beir · https://arxiv.org/abs/2212.10496 · https://arxiv.org/abs/2401.15884 · https://console.groq.com/docs/quickstart
