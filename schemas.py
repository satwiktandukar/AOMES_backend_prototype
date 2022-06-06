from typing import Optional
from pydantic import BaseModel

from blog.database import Base

class MBBS(BaseModel):
    question: str
    answer_1: str
    answer_2: str
    answer_3: str
    answer_4: str
    correct: str

    class Config:
        orm_mode = True

class Nursing_License(BaseModel):
    question: str
    answer_1: str 
    answer_2: str 
    answer_3: str 
    answer_4: str 
    correct: str

class BMLT(BaseModel):
    question: str
    answer_1: str 
    answer_2: str 
    answer_3: str 
    answer_4: str 
    correct: str

class Agriculture(BaseModel):
    question: str
    answer_1: str 
    answer_2: str 
    answer_3: str 
    answer_4: str 
    correct: str


class Login(BaseModel):
    phone: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    phone: Optional[str] = None


