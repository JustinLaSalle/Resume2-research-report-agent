"""
Research & Report Agent

Give it an open-ended topic, and the agent autonomously searches the
web, gathers information from multiple sources, and synthesizes a
structured written report — with citations.

This demonstrates a different kind of agentic reasoning than a fixed
support/sales workflow: instead of calling from a small set of
predefined tools in a predictable order, the agent decides how many
searches to run, what to search for next based on what it's already
found, and when it has enough information to write the report.

Install:
    pip install anthropic

Run:
    export ANTHROPIC_API_KEY=your_key_here
    python agent.py
"""

import anthropic

client = anthropic.Anthropic()

SYSTEM_PROMPT = (
    "You are a research agent. Given a topic, use web search to gather "
    "current, credible information from multiple sources before writing "
    "anything. Search as many times as needed to cover the topic "
    "properly — don't settle for a single search if the topic has "
    "multiple angles (e.g. background, current state, different "
    "viewpoints). Once you have enough to write a well-supported "
    "report, stop searching and write it.\n\n"
    "Structure the final report as:\n"
    "1. A short executive summary (2-3 sentences)\n"
    "2. Key findings, organized under clear subheadings\n"
    "3. Any notable disagreements or uncertainty between sources\n"
    "Cite sources inline as you go."
)


def research_topic(topic: str) -> str:
    messages = [{"role": "user", "content": f"Research this topic and write a report: {topic}"}]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=messages,
    )

    # The API runs the search loop server-side for the web_search tool,
    # so response.content already contains the final report text
    # (interleaved with search-result blocks Anthropic returns for
    # transparency/citation purposes).
    report_text = "".join(
        block.text for block in response.content if block.type == "text"
    )
    return report_text


if __name__ == "__main__":
    topic = "The current state of small business adoption of AI automation tools"
    print(f"Researching: {topic}\n")
    report = research_topic(topic)
    print(report)

    with open("sample_report.md", "w") as f:
        f.write(f"# Research Report: {topic}\n\n{report}")
    print("\nSaved full report to sample_report.md")
