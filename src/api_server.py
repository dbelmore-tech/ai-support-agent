from fastapi import FastAPI
from pydantic import BaseModel
@app.get("/")
def home():
    return {"message": "RemoteRig AI Support Agent is online. Use /docs to test the API."}


app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat_endpoint(message: Message):
    return {"response": "API server is running. You sent: " + message.text}
