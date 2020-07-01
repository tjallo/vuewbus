# Import local dependencies
from api.game import cards as Cards

# Player Object [name, drinks, [cards], id]
players = []

def addPlayer(name):
    id = len(players)
    players.append([name, 0, [], id])
    return f"Added {name}"

def getAllPlayerObjects():
    return players

def getAllPlayerNames():
    arr = []
    for i in range(len(players)):
        arr.append(players[i][0])
    return arr

def getAndAddCardToPlayer(playerID):
    card = Cards.getCard()
    players[playerID][2].append(card)
    return card

def returnPlayerById(playerID):
    return players[playerID][0]
