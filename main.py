# Import Dependencies 
from fastapi import FastAPI
import json, math
from fastapi.middleware.cors import CORSMiddleware

# Import Local Dependencies
from api.game import cards as Cards
from api.game import players as Players
from api.game import turncount as Turn


def addMockupPlayers():
    Players.addPlayer("Henk")
    Players.addPlayer("Klaas")
    Players.addPlayer("Piet")
    Players.addPlayer("Jantje")

def getPlayerTurn():
    Turn.modulus = len(Players.getAllPlayerNames())
    if Turn.n == 0:
        Turn.n =+ 1
        return 0, 0
    turn1 = Turn.n % Turn.modulus
    cardRound = math.floor(Turn.n / Turn.modulus)
    Turn.n += 1
    return turn1, cardRound
    

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



"""

ROUND 1

"""

@app.get('/round1/1/')
async def getCard1():
    turn, cardTurn = getPlayerTurn()
    card = Players.getAndAddCardToPlayer(turn)
    card = Cards.cardParser(card[0], card[1])
    player = Players.returnPlayerById(turn)
    return [player, cardTurn, card]

addMockupPlayers()