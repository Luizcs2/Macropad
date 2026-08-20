from pydantic import BaseModel

class CommandReq(BaseModel):
    name:str