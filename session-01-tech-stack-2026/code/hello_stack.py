"""hello_stack.py — the WHOLE agent stack in one screen.

This tiny agent answers a question that needs a tool. As it runs, it prints a
labelled banner for each of the 7 core components, so you can literally SEE the
stack execute. We build each of these up properly across the series — here they
all appear at once, in ~60 lines.

    1 MODEL  2 MEMORY  3 TOOLS  4 ORCHESTRATION
    5 GUARDRAILS  6 HUMAN-IN-THE-LOOP  7 OBSERVABILITY

Run:  python hello_stack.py
"""

import time

from llm import chat, text_of

# ── 3 · TOOLS ────────────────────────────────────────────────────────────────
# A tool is a name + description + input schema the model sees, plus a function
# our code runs (the model never runs code itself).
def calculator(expression: str) -> float:
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        raise ValueError(f"unsafe: {expression!r}")
    return eval(expression)  # noqa: S307 — restricted to arithmetic


TOOLS = [{
    "name": "calculator",
    "description": "Evaluate an arithmetic expression like '23*17 + 8'.",
    "input_schema": {"type": "object",
                     "properties": {"expression": {"type": "string"}},
                     "required": ["expression"]},
}]
RISKY_TOOLS: set[str] = set()  # none here; but this is where HITL would trigger

SYSTEM = "You are a precise assistant. Use the calculator tool for any arithmetic."
TASK = "What is 23 * 17 + 8? Use the tool, then state the result."
MAX_STEPS = 5  # ── 5 · GUARDRAILS: the loop can never run forever ──


def banner(n, name):
    print(f"\n\033[1m[{n} {name}]\033[0m")


def main():
    print("=" * 68)
    print("hello_stack — watch all 7 components run")
    print("=" * 68)

    # ── 2 · MEMORY: the conversation history we carry forward each turn ──
    banner(2, "MEMORY"); print("  starting empty message history")
    messages = [{"role": "user", "content": TASK}]

    # ── 4 · ORCHESTRATION: the reason→act→observe loop ──
    banner(4, "ORCHESTRATION"); print("  running the agent loop")
    for step in range(1, MAX_STEPS + 1):
        # ── 1 · MODEL ──
        banner(1, "MODEL"); print(f"  step {step}: asking the model to reason")
        t0 = time.time()
        resp = chat(messages=messages, system=SYSTEM, tools=TOOLS)
        # ── 7 · OBSERVABILITY: trace latency + tokens every call ──
        u = resp.usage
        banner(7, "OBSERVABILITY")
        print(f"  {time.time()-t0:.2f}s · in={u.input_tokens} out={u.output_tokens}"
              f" tok · stop={resp.stop_reason}")

        thinking = text_of(resp).strip()
        if thinking:
            print(f"  🧠 {thinking}")

        if resp.stop_reason != "tool_use":
            print("\n" + "=" * 68)
            print("✅ FINAL:", thinking)
            print("You just watched Model, Memory, Tools, Orchestration, Guardrails,")
            print("Human-in-the-loop, and Observability — the whole 2026 stack.")
            return

        messages.append({"role": "assistant", "content": resp.content})
        results = []
        for block in resp.content:
            if block.type != "tool_use":
                continue
            # ── 6 · HUMAN-IN-THE-LOOP: gate risky tools (none today) ──
            if block.name in RISKY_TOOLS:
                banner(6, "HUMAN-IN-THE-LOOP")
                if input(f"  approve {block.name}? [y/N] ").lower() != "y":
                    results.append({"type": "tool_result", "tool_use_id": block.id,
                                    "content": "denied by human", "is_error": True})
                    continue
            # ── 3 · TOOLS: run the requested tool ──
            banner(3, "TOOLS")
            out = calculator(**block.input)
            print(f"  ran {block.name}({block.input}) → {out}")
            results.append({"type": "tool_result", "tool_use_id": block.id,
                            "content": str(out)})
        messages.append({"role": "user", "content": results})

    print("\n⚠️  hit MAX_STEPS (guardrail) before finishing")


if __name__ == "__main__":
    main()
