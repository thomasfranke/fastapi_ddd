from pydantic import BaseModel

class Example(BaseModel):
    id: int
    message: str
