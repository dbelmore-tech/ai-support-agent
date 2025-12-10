# AI Support Agent (RemoteRig Web Edition)

This project began as a small, portfolio-friendly example of an LLM-powered support agent, and has now evolved into a web-based interactive AI support tool suitable for real-world testing.

It demonstrates how a technical support or solutions engineer might use a large language model to:

* Classify incoming support issues
* Generate troubleshooting steps
* Suggest follow-up questions
* Provide real-time conversational support
* Power a lightweight, branded chat interface

The design is intentionally simple but shows the core ideas behind agentic workflows, prompt design, web-based LLM orchestration, and multi-modal deployment (CLI + API + web UI).

---

## What It Does

Given a short description of a user’s problem, the agent will:

1. Generate a troubleshooting response via the OpenAI API
2. Provide clear, actionable steps
3. Ask useful follow-up questions
4. Act as a real-time support assistant through a clean web UI

Two interaction modes are available:

1. Web Chat Interface (FastAPI)

* Chat bubbles
* “AI is thinking…” indicator
* RemoteRig gradient background
* Initial cold-start notice

2. Console Version
   A simple CLI tool that logs interactions in logs/ for debugging or analysis.

---

## Project Structure

ai-support-agent/
├── README.md
├── requirements.txt
├── logs/
│    └── ... session logs
└── src/
├── agent.py        (console version)
├── agent_core.py   (shared AI logic)
├── api_server.py   (FastAPI backend)
└── chat.html       (web UI)

---

## Running Locally

1. Install dependencies
   pip install -r requirements.txt

2. Add your API key
   Create a file named .env with this inside:
   OPENAI_API_KEY=your_key_here

3. Start the web server
   uvicorn src.api_server:app --reload
   Then open:
   [http://localhost:8000/chat-ui](http://localhost:8000/chat-ui)

4. Run the console version
   python src/agent.py

---

## Deployment

This project is currently deployed on Render, using:

* uvicorn
* FastAPI
* Environment variable support
* Automatic redeploy on GitHub push

Note: The first request may take a few seconds due to cold-start behavior on free hosting.

---

## Notes

* This is an early-stage prototype; UI and backend behavior may evolve quickly.
* Long-term goal: support specialized personas (tech support, solar, electrical, heating, RV systems, etc.).
* Feedback is welcome from testers.

---

## License

MIT License — free to modify and extend.

---