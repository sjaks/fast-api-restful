from pydantic import BaseModel

class Train(BaseModel):
    manufacturer: str
    type: str
    year: int
    id: str = ""
