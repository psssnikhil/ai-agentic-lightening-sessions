# Session 1 — Restructured Plan (40 min)

**Goal:** One energetic lap around the whole agent stack — what each part does, how they connect, and where they land in a real production agency system.

**Audience:** Engineers & technical PMs. No prior agent experience.

**Design principles**
- **Journey, not encyclopedia** — cut reference dumps (8-layer taxonomy, protocol deep-dive, future bets).
- **One line per component** — name + job + connection to the next box.
- **Visual-first** — fragments build the stack; diagrams carry the story.
- **Production anchor** — the closing diagram is a concrete agency system, not abstract boxes.
- **40 minutes tight** — demo stays; sweep the stack map in ~90 seconds.

---

## Flow (11 slides · ~40 min)

| Time | Slide | What happens |
|------|-------|--------------|
| 0:00 | **1 · Title** | Hook: "In 40 minutes you'll see the whole board — and watch it run." |
| 0:02 | **2 · The shift** | 2023 = "can the model do it?" → 2026 = "can I make it reliable?" Harness = the stack. |
| 0:04 | **3 · Agent in 30s** | Model in a loop + tools + goal. "Who decides the next step?" |
| 0:06 | **4 · 7 components** | Fragment build — one card at a time. Core → Control → Trust colours. |
| 0:12 | **5 · One request, 7 touchpoints** | Journey diagram: a single user ask flows through every component (loop visible). |
| 0:16 | **6 · 2026 stack map** | One-page bento — sweep categories, don't read logos (~90s). |
| 0:19 | **7 · 2023→2026** | 4-stop timeline — each wave added a layer. Punchline: reliability era. |
| 0:22 | **8 · LIVE demo** | `hello_stack.py` — narrate labelled banners (~5 min). |
| 0:27 | **9 · Grow into production** | Prototype → Feature → Production. Add a box when a failure demands it. |
| 0:29 | **10 · Production agency system** | **Hero diagram** — client brief → research → draft → review → human approve → ship; all 7 components + tech stack mapped. |
| 0:36 | **11 · Series + recap** | Sessions 2–6 build this for real. Five takeaways. Q&A buffer. |

**Cut from old deck (available in `diagrams/` if needed later):**
- 8-layer architecture slide — too academic for opener
- Protocol deep-dive — MCP/A2A folded into stack map + agency diagram
- Agent patterns grid — patterns referenced on agency diagram + series slide
- "Where it's heading" — future bets; low engagement per brief

---

## The 7 components — one-liners (presenter script)

| # | Component | One-liner | Connects to |
|---|-----------|-----------|-------------|
| 1 | **Model** | The brain that reasons and picks the next move | Reads memory, may call tools |
| 2 | **Memory** | Everything the agent remembers across turns | Feeds the model each loop |
| 3 | **Tools** | Hands that act on the world (search, code, APIs) | Results flow back to memory |
| 4 | **Orchestration** | The loop that coordinates steps (and agents) | Wraps model + tools + memory |
| 5 | **Guardrails** | Hard limits — budgets, policies, step caps | Stops bad runs before damage |
| 6 | **Human-in-the-loop** | Approval gate for high-stakes actions | Sits on risky tool calls |
| 7 | **Observability** | Traces, tokens, evals — trust in production | Wraps every call |

---

## Evaluation (post-restructure)

| Criterion | Before | After |
|-----------|--------|-------|
| **Time fit** | 45–55 min (7 dense diagrams) | 40 min with buffer |
| **Engagement** | Reference-heavy mid-section | Fragment builds + journey + hero finale |
| **Component depth** | Good one-liners but scattered | One-liners + connection slide + mapped on agency diagram |
| **Production relevance** | Abstract stack boxes | Concrete agency pipeline with tech labels |
| **Visual quality** | Strong SVGs, too many | Fewer, sharper; finale is the screenshot slide |
| **Series hook** | Patterns slide doubled as roadmap | Agency diagram → "we build this in Sessions 2–6" |

---

## Files changed

- `deck/index.html` — restructured slides
- `diagrams/request-journey.svg` — new: one request through 7 components
- `diagrams/production-agency-system.svg` — new: hero finale
- `RUNBOOK.md` — updated timing
- `SESSION-01-PLAN.md` — this file
