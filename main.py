# Import Dependencies 
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

# Import Local Dependencies
from api.game import cards as Cards
from api.game import players as Players

#Setup FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

"""

PLAYERS

"""
@app.post("/addPlayer/")
async def addPlayer(playername):
    Players.addPlayer(playername)
    return {f'{playername} was added'}

@app.get("/getPlayerObjects/")
async def getPlayerObjects():
    return Players.getAllPlayerObjects()

@app.get("/getPlayerNames/")
async def getPlayerNames():
    return Players.getAllPlayerNames()

"""

CARDS

"""

@app.get("/getCard/")
async def getCardForPlayer(playerID):
    card = Players.getAndAddCardToPlayer(playerID)    
    return card

@app.post("/giveMePlayerData/")
async def giveMePlayerData(data):
    data = json.loads(data)
    for name in data:
        Players.addPlayer(name)
    return(data)