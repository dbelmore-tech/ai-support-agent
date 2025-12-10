from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.agent_core import run_agent
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Your RemoteRig AI Support Agent is online. Use /docs to test the API."}

# --- New code for chat UI ---
app.mount("/static", StaticFiles(directory="src"), name="static")

@app.get("/chat-ui", response_class=HTMLResponse)
def chat_ui():
    file_path = os.path.join("src", "chat.html")
    with open(file_path, "r") as f:
        return f.read()
# --- End of new code ---

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat_endpoint(message: Message):
    reply = run_agent(message.text)
    return {"response": reply}
