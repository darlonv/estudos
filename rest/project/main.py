from fastapi import FastAPI
from pydantic import BaseModel

class ItemIn(BaseModel):
	base: int
	expoente: int

class ItemOut(BaseModel):
	base: int | None = None
	expoente: int | None = None
	potencia: int | None = None

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/quad/{val}")
def quad(val: int):
	return {val: val**2}

@app.get("/pow/{val}/{power}")
def pow(val:int, power:int):
	return {val**power}

@app.post('/pow/', response_model = ItemOut)
async def pow(item: ItemIn):
	saida = ItemOut()
	saida.base, saida.expoente = item.base, item.expoente
	saida.potencia = item.base ** item.expoente
	return saida