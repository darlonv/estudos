from fastapi import FastAPI

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
