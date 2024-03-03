from pydantic import BaseModel


class HelloReply(BaseModel):
    message: str
