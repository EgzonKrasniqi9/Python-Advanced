from pydantic import BaseModel

class MovieCreate(BaseModel):
    title:str
    directory: str

class Movie(MovieCreate):
    id:int

