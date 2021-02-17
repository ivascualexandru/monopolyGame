from player import Player
from board import *
import random
import os


os.system('cls')  # clear screen before running file


def outputPlayerInfo(playerNum):
  #TODO fix bug related to this not being displayed at all
  for i in range(playerNum):
    print("Player " + str(i))
    print("Name: " + players[i].name + "     Money: " + str(players[i].money))
    print("Position: " + players[i].tile.name)

def rollDice():
    #TODO make it so that you actually roll twice, and if the results match,
    #recursively call it again with depth+1 until we get to 3 or we stop rolling doubles
    randomNum = random.randint(1,6)
    print("Rolled a " + str(int(randomNum)) + "!")
    return randomNum

#INITIALIZING NUMBER OF PLAYERS
strPlayerNum = input("Hello and welcome to another game of Monopoly! How many players will it be?")
playerNum = int(strPlayerNum)
players = []
for i in range(playerNum):
  playerName = input("Player " + str(i+1) + "'s name is the following: ")
  players.append(Player(2000, playerName))

#INITIALIZING THE TILES
tiles = []
for i in range(39):
  tiles.append(Tile(namesForTiles[i],pricesForTiles[i],0,0,i)) #name, price, owned by, no of houses, id

while True:
  #CHECKING IF GAME IS OVER
  remainingPlayers = playerNum
  for j in range(playerNum):
    if (players[j].money == 0):
      remainingPlayers-=1
  print(str(remainingPlayers) + " players left.")
  if (remainingPlayers == 1):
    for j in range(playerNum):
      if (players[j].money != 0):
        print(players[j].name + "WON! A round of applause.")
        break

  outputPlayerInfo
  #IF GAME IS NOT OVER, ROLL THE DICE
  for i in range(playerNum):
    print("Player " + str(i+1) + "'s turn")
    playerDecision = input("Roll / Build / End:")
    if (playerDecision == "Roll"):
      players[i].moveSpaces(rollDice())
      print(tiles[players[i].tile].name)
      if (tiles[players[i].tile].ownedBy == 0): #IF TILE ISN'T ALREADY OWNED BY ANYONE IN THE GAME
        print("It appears the tile you landed on (" + tiles[players[i].tile].name + ") isn't owned by anyone, and costs " + str(tiles[players[i].tile].price))
        buy = input("Do you want to buy it? [Y/N]")
        if (buy == "Y"):
          players[i].money -= tiles[players[i].tile].price
          tiles[players[i].tile].ownedBy = i
          print("Tile " + tiles[players[i].tile].name + "has been bought by player " + str(i))
    '''
    TODO: 
    IF BOARD[players[i].tile] NOT OWNED
    PROMPT PLAYER TO MAKE A CHOICE
    BUY OR NOT (MAYBE AUCTION)
    '''