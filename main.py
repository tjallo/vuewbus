# Import Dependencies 
from fastapi import FastAPI

# Import Local Dependencies
from api.game import cards as cards

#Setup FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}