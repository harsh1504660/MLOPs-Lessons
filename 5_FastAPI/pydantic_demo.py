from pydantic import BaseModel

data = {
    "name": "Murthy",
    "age": "28",
    "course": "MLOps BootCamp",
    "ratings": [4, 4, "4", "5", 4]
}

class Instrucotr(BaseModel):
    name : str
    age : int
    course : str
    ratings : list[int] = []

user = Instrucotr(**data)

print(f" found a instructor :{user}")