from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from common.response import get_reply


class Conversation(BaseModel):
    user_id: int
    sentence: str


app = FastAPI()


@app.get("/test")
def test():
    return {"message": "Server running"}


@app.post("/conversation")
def get_response(conversation: Conversation):
    res = get_reply(user_id=conversation.user_id,
                    sentence=conversation.sentence)
    return {"text": res}
