from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat_endpoint(message: Message):
    return {"response": "API server is running. You sent: " + message.text}
