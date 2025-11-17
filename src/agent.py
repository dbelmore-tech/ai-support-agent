"""
AI Support Agent Simulator

Usage (from repo root):

    python src/agent.py

Then follow the prompts.
"""

from pathlib import Path

from prompts import (
    BASE_SYSTEM_PROMPT,
    CLASSIFICATION_PROMPT,
    TROUBLESHOOTING_PROMPT,
)
from utils import LLMClient, parse_json_safely, start_log_session, append_log


def classify_issue(llm: LLMClient, issue: str) -> dict:
    prompt = CLASSIFICATION_PROMPT.format(issue=issue)
    messages = [
        {"role": "system", "content": BASE_SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]
    raw = llm.chat(messages)
    return parse_json_safely(raw)


def generate_troubleshooting_plan(
    llm: LLMClient,
    issue: str,
    classification: dict,
) -> str:
    category = classification.get("category", "other")
    explanation = classification.get("explanation") or classification.get("raw_text", "")
    prompt = TROUBLESHOOTING_PROMPT.format(
        issue=issue,
        category=category,
        classification_explanation=explanation,
    )
    messages = [
        {"role": "system", "content": BASE_SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]
    return llm.chat(messages)


def main():
    print("=== AI Support Agent Simulator ===")
    print("Type a short description of a user's issue.")
    print("Type 'quit' to exit.\n")

    try:
        llm = LLMClient()
    except RuntimeError as e:
        print(f"Error: {e}")
        print("Tip: create a .env file with OPENAI_API_KEY=your_key_here")
        return

    session_log: Path = start_log_session()
    append_log(session_log, "=== New session started ===")

    while True:
        issue = input("\nUser issue: ").strip()
        if not issue:
            print("Please enter a description, or type 'quit' to exit.")
            continue
        if issue.lower() in {"quit", "exit"}:
            print("Goodbye.")
            append_log(session_log, "=== Session ended by user ===")
            break

        append_log(session_log, f"\nUSER_ISSUE: {issue}")

        print("\n[1/3] Classifying issue...")
        classification = classify_issue(llm, issue)
        append_log(session_log, f"CLASSIFICATION: {classification}")

        category = classification.get("category", "other")
        explanation = classification.get("explanation") or classification.get("raw_text", "")

        print(f" → Category: {category}")
        if explanation:
            print(f" → Reason: {explanation}")

        print("\n[2/3] Generating troubleshooting plan...")
        plan = generate_troubleshooting_plan(llm, issue, classification)
        append_log(session_log, "TROUBLESHOOTING_PLAN:\n" + plan)

        print("\n[3/3] Suggested response & steps:\n")
        print(plan)
        print("\n(Response also saved to log file.)")


if __name__ == "__main__":
    main()

