# Session 1 — Runbook (Presenter Guide)

**The AI Agent Tech Stack in 2026** · **40 min** · single `ANTHROPIC_API_KEY`

Restructured opener: agent definition → 7 components (names only) → internals table → connection diagram → ecosystem map → live demo → **use-case-first production finale**. Each slide has one job — no repeated definitions.

Full plan: `SESSION-01-PLAN.md`

---

## 0. Files

```
session-01-tech-stack-2026/
├── SESSION-01-PLAN.md       # restructure rationale + evaluation
├── deck/index.html          # 14 slides (40 min)
├── diagrams/
│   ├── request-journey.svg           # how 7 components connect (slide 6)
│   ├── production-agency-system.svg  # alternate on disk
│   ├── components-flow.svg         # alternate (on disk)
│   ├── stack-2026-full.svg           # alternate full bento
│   └── …
├── code/
│   ├── hello_stack.py
│   ├── llm.py
│   └── …
└── RUNBOOK.md
```

---

## 1. One-time setup

```bash
cd session-01-tech-stack-2026/code
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # paste ANTHROPIC_API_KEY
python hello_stack.py   # smoke test
```

Deck: open `deck/index.html` in Chrome. `S` = speaker notes, `F` = fullscreen.
PDF: `deck/index.html?print-pdf` → Print → Save as PDF.

---

## 2. Minute-by-minute (40 min)

| Time | Slide | Do / say |
|------|-------|----------|
| 0:00 | Title | "40 minutes — whole board, then watch it run." |
| 0:02 | The shift | 2026 = reliability era; the harness. |
| 0:04 | Agent in 30s | "Who decides the next step?" — definition only. |
| 0:06 | **7 components** | Names + one job each. No connections yet. |
| 0:09 | **Internals table** | Types · internals · fits — cheat sheet (~20s/row). |
| 0:12 | **Full picture** | Where deployment/monitoring/RAG live + types in depth. |
| 0:15 | **Request journey** | Trace arrows only — don't re-define boxes. |
| 0:16 | 2026 stack map | Sweep ecosystem layers in ~60s. |
| 0:17 | **DEMO** | `python hello_stack.py` — narrate banners (~5 min). |
| 0:22 | Grow into production | Prototype → feature → production. |
| 0:24 | **What we're building** | Read example brief · input / process / output. |
| 0:27 | **Production pipeline** | Walk pipeline + component table. |
| 0:34 | **Summary + next** | Today's takeaways · Session 2 preview. |
| 0:37 | Q&A | Buffer. |

---

## 3. Internals slide script (slide 5 · ~4 min)

Click through table fragments. Per row, say:
1. **Model** — frontier vs open; worker vs reviewer; prompt+messages in → text or tool_use out
2. **Memory** — thread vs vector RAG vs files; injected context each turn
3. **Tools** — search/code/API/MCP; schema contract → execute → result back
4. **Orchestration** — ReAct vs pipeline vs supervisor; graph picks next step
5. **Guardrails** — caps, budget, injection filter; checks before/after calls
6. **HITL** — approve tool or publish; pause → human → resume
7. **Observability** — traces, metrics, offline/online eval; log every hop

Land: *"Slide 6 shows where deployment, monitoring, and RAG fit — and expands every type."*

## 4. Full picture slide (slide 6 · ~3 min)

**Top — cross-cutting (not an 8th box):**
- Prompt engineering → ① · RAG → ② · MCP → ③ · structured output → ⑤
- Monitoring & eval CI → ⑦ · deployment → ④+⑦ · governance → ⑤ + platform

**Bottom table — types in depth:** scan Models/Memory/Tools/Orchestration/Obs rows. Land: *monitoring is inside Observability, not a separate component.*

## 5. Hero slides (11–12 · use case + pipeline)

**Slide 11 — read the brief aloud:**

> Example: "Write a launch post for Product X. Tone: confident, not salesy. Cite two sources. PM must approve before publish."

Land: Input → Process → Output. No fragments — content shows immediately.

**Slide 12 — two passes:**

1. **Pipeline (top):** Brief → Orchestrator → Research → Writer → Reviewer → PM → CMS. Numbers on agents show which components that step uses.

2. **Table (bottom):** One concrete example per component for THIS system. Do not re-read slide 5 types.

---

## 6. The demo (~5 min)

```bash
python hello_stack.py
```

Narrate banners: `[2 MEMORY]` → `[4 ORCHESTRATION]` → `[1 MODEL]` → `[7 OBSERVABILITY]` → `[3 TOOLS]` → answer `399`.

Fallback: walk code in editor; answer is deterministic `23 * 17 + 8 = 399`.

---

## 7. Anticipated questions

- **"Which framework?"** — Learn the category. Plain loop today; ideas port to LangGraph/CrewAI/etc.
- **"Need all 7 day one?"** — No. Prototype with 3; grow when failures demand it.
- **"MCP required?"** — Emerging standard for tool boundary; Session 6 goes deep.
- **"Isn't this just ML ops?"** — New layers: orchestration loops, agent observability, evals for nondeterminism.
