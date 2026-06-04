from pydantic import BaseModel

class RecipeCreate(BaseModel):
    title:str
    directory: str

class Recipe(RecipeCreate):
    id:int

