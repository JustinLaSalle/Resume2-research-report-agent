# Research & Report Agent

An autonomous AI agent that researches an open-ended topic and produces a structured, cited report — built with the [Claude API](https://docs.claude.com) and its web search tool.

## The problem

Research is one of the most time-consuming parts of many jobs — sales prep, market analysis, competitive research, due diligence. It's also one of the hardest tasks to automate well, because it's open-ended: unlike a support ticket, there's no fixed set of steps. A good researcher doesn't just run one search; they follow up on what they find, check multiple angles, and know when they've gathered enough to write something useful.

## What this agent does

Given a single topic, the agent:

1. **Decides what to search for** — and how many searches are needed, based on the topic's complexity
2. **Follows up dynamically** — if an early search surfaces something worth digging into further, it searches again rather than stopping at one result
3. **Recognizes when it has enough** — stops searching once it can support a well-rounded report, rather than running forever or stopping too early
4. **Writes a structured report** — executive summary, key findings under subheadings, and any notable disagreement between sources, with inline citations

This is a different kind of "agentic" than a fixed workflow like a ticket router: there's no predetermined sequence of tool calls. The model is making judgment calls about *its own research process*, not just executing a script.

## Example use

```python
from research_agent import research_topic

report = research_topic("The current state of small business adoption of AI automation tools")
print(report)
```

Produces a multi-section markdown report, saved to `sample_report.md`.

## How it works

- Uses the Claude API's built-in [web search tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool) — search execution and result retrieval happen server-side, so the agent can run as many searches as the topic needs without extra orchestration code
- A single system prompt defines the research process and report structure — no hardcoded step sequence
- Output is saved as a standalone markdown file, easy to hand off or drop into a doc

## Setup

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
python agent.py
```

## Tech

- Python
- [Anthropic Claude API](https://docs.claude.com) (Claude Sonnet)
- Web search tool
