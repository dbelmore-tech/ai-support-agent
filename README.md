# AI Support Agent Simulator

This project is a small, portfolio-friendly example of an **LLM-powered support agent**. It simulates how a technical support or solutions engineer might use a large language model to:

- Classify incoming support issues  
- Generate troubleshooting steps  
- Suggest follow-up questions  
- Recommend whether to escalate and to whom  

It’s intentionally simple, but it shows the core ideas behind **agentic workflows**, **prompt design**, and **LLM orchestration** that are relevant to modern AI-powered support and solutions roles.

---

## 🔍 What It Does

Given a short description of a user’s problem, the agent will:

1. **Classify the issue**  
   (e.g., account_access, billing_or_payments, configuration_or_setup, performance_or_slow, data_or_integrations, other)

2. **Explain the classification**  
   Why it thinks this is the right category.

3. **Generate a troubleshooting plan** that includes:
   - A brief, empathetic summary of the problem  
   - Concrete troubleshooting steps  
   - Helpful follow-up questions  
   - A recommendation about escalation  

All interactions are logged to a timestamped file in `logs/`.

---

## 🧱 Project Structure

```text
ai-support-agent/
  ├── README.md
  ├── requirements.txt
  ├── logs/
  │    └── ... (session logs)
  └── src/
       ├── agent.py        # Main CLI entry point
       ├── prompts.py      # System and task prompt templates
       └── utils.py        # LLM client + logging helpers
