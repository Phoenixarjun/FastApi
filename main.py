from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
  return {"data": {"message": "Hello, World!"}} 



@app.get("/hello/{id}")
def hello(id: int):
  return {"data": {"message": f"Hello, {id}!"}}


