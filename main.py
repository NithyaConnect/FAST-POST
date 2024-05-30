from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/process-message/")
async def process_message(message: Message):
    response_message = f"{message.text} success"
    return {"response_message": response_message}

