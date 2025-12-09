from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RemoteRig AI Support Agent is online. Use /docs to test the API."}

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat_endpoint(message: Message):
    return {"response": "API server is running. You sent: " + message.text}
