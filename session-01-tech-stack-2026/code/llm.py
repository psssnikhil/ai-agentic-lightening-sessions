"""Thin, swappable LLM wrapper (the Model layer of the stack).

Everything in the course talks to the model through this one file. Swap the body
to change providers and every demo keeps working.

Provider: Anthropic Claude · Model: claude-sonnet-5 (fast) / claude-opus-4-8 (deep)
"""

import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

_client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
MODEL = os.environ.get("MODEL", "claude-sonnet-5")


def chat(messages, system=None, tools=None, max_tokens=1024, model=None):
    """Send messages to the model; return the raw Anthropic response object."""
    kwargs = {"model": model or MODEL, "max_tokens": max_tokens, "messages": messages}
    if system:
        kwargs["system"] = system
    if tools:
        kwargs["tools"] = tools
    return _client.messages.create(**kwargs)


def text_of(response):
    """Concatenate all text blocks from a response."""
    return "".join(b.text for b in response.content if getattr(b, "type", None) == "text")
