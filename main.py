# Import Dependencies 
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

# Import Local Dependencies
from api.game import cards as Cards
from api.game import players as Players

turnCount = 0
modulusDivider = 0

def getPlayerTurn(tc, md):
    if tc == 0:
        turnCount =+ 1
        return 0
    turn = tc % md
    turnCount =+ 1
    return turn

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
    modulusDivider = len(data)
    return(data)



"""

ROUND 1

"""

@app.get('/round1/1/')
async def getCard1():
    turn = getPlayerTurn(turnCount, modulusDivider)
    card = Players.getAndAddCardToPlayer(turn)
    player = Players.returnPlayerById(turn)

    return {"card": Cards.cardParser(card[0], card[1]), "Turn": turn, "Turncount": turnCount, "Player": player}