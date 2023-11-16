from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from common.response import get_reply
import logging


class Conversation(BaseModel):
    user_id: int
    sentence: str
    character_name: str

    def __str__(self):
        return 'user_id:%d sentence:%s character_name:%s' % (self.user_id, self.sentence, self.character_name)


app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s"
)


@app.get("/test")
def test():
    return {"message": "Server running"}


@app.post("/conversation")
def get_response(conversation: Conversation):
    logging.debug('Request content: ' + str(conversation))
    res = get_reply(user_id=str(conversation.user_id),
                    sentence=conversation.sentence, character_name=conversation.character_name)
    return {"text": res}
