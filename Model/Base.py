from pydantic import BaseModel
from datetime import datetime

class Base(BaseModel):
    created: datetime
    edited: datetime
    url: str