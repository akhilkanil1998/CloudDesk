# imports the Fast Api package
from fastapi import FastAPI

# Instance of FastAPI
app = FastAPI()

@app.get("/")
def greet():
    return "Hi User"