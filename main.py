from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from common.response import get_reply


class Conversation(BaseModel):
    user_id: int
    sentence: str
    character_name: str


app = FastAPI()


@app.get("/test")
def test():
    return {"message": "Server running"}


@app.post("/conversation")
def get_response(conversation: Conversation):
    res = get_reply(user_id=str(conversation.user_id),
                    sentence=conversation.sentence,character_name=conversation.character_name)
    return {"text": res}
