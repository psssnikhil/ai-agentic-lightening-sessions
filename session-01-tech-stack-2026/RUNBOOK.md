# Session 1 — Runbook (Presenter Guide)

**The AI Agent Tech Stack in 2026** · **40 min** · single `ANTHROPIC_API_KEY`

Full plan: `SESSION-01-PLAN.md`

---

## 0. Files

```
session-01-tech-stack-2026/
├── deck/index.html          # 14 slides (40 min)
├── code/hello_stack.py
└── RUNBOOK.md
```

Deck: open `deck/index.html` in Chrome. `S` = speaker notes, `F` = fullscreen.

---

## 1. Slide guide (14 slides)

| # | Title on slide | Job |
|---|----------------|-----|
| 1 | Welcome · The AI Agent Tech Stack in 2026 | Intro you + session title |
| 2 | Production is the hard part now | 2026 shift · harness |
| 3 | What makes it an agent? | One-line test |
| 4 | Seven components · one job each | Name the 7 boxes |
| 5 | Types, internals & how each fits | Cheat sheet (screenshot) |
| 6 | Where deployment, RAG & monitoring fit | Mapping table only |
| 7 | One request through the loop | Connection diagram (names only) |
| 8 | The 2026 vendor landscape | Ecosystem sweep |
| 9 | All seven components in one script | Run `hello_stack.py` |
| 10 | Start with three · grow to seven | Adoption path |
| 11 | Use case: research + draft a campaign post | Example brief |
| 12 | The production pipeline | Pipeline + component table (screenshot) |
| 13 | What we covered · what's next | 4 takeaways + series arc (S2–S6) |
| 14 | Questions? | Q&A |

---

## 2. Minute-by-minute (40 min)

| Time | Slide | Do / say |
|------|-------|----------|
| 0:00 | 1 Welcome | Who you are · session title (~60 sec). |
| 0:01 | 2 Production shift | Harness · reliability era. |
| 0:03 | 3 Agent definition | "Who decides the next step?" |
| 0:05 | 4 Seven components | Click fragments — one job each. |
| 0:08 | 5 Internals table | ~20 sec/row · screenshot slide. |
| 0:11 | 6 Wider stack map | Monitoring = box 7, not box 8. |
| 0:13 | 7 Request loop | Trace arrows · names only on boxes. |
| 0:15 | 8 Vendor landscape | Sweep layers · don't read logos. |
| 0:17 | 9 **DEMO** | `python hello_stack.py` (~5 min). |
| 0:22 | 10 Adoption | Prototype → production. |
| 0:24 | 11 Use case | Read example brief aloud. |
| 0:27 | 12 Pipeline | Walk left→right · scan table. |
| 0:34 | 13 Wrap-up | 4 takeaways · Session 2 preview. |
| 0:37 | 14 Q&A | Buffer. |

---

## 3. Key scripts

**Slide 5 — internals table:** Click fragments. Land: *"Slide 6 shows where deployment and monitoring fit."*

**Slide 6 — mapping only:** Scan table. Don't repeat slide 5 types.

**Slide 11 — read brief:**

> "Write a launch post for Product X. Tone: confident, not salesy. Cite two sources. PM must approve before publish."

**Slide 12 — pipeline:** Brief → Orchestrator → Research → Writer → Reviewer → PM → CMS.

**Slide 13 — series arc (read order):**

1. **Session 1** *(today)* — map the stack  
2. **Session 2** — build your first agent  
3. **Session 3** — RAG: beginner → production  
4. **Session 4** — research agent  
5. **Session 5** — building your own agentic system  
6. **Session 6** — ship the production pipeline  

Tease S2: hands-on coding agent · Python + API key ready.

**Slide 9 — demo:**

```bash
cd session-01-tech-stack-2026/code && python hello_stack.py
```

Narrate banners → answer `399`. Fallback: walk code in editor.

---

## 4. Anticipated questions

- **"Which framework?"** — Learn the category; ideas port to any runtime.
- **"Need all 7 day one?"** — No. Start with 3; grow when failures demand it.
- **"Where does monitoring fit?"** — Component 7 · Observability (slide 6).
