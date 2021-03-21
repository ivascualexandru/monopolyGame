from player import *
from board import *
from moreFunctions import *
import os


os.system('cls')  # clear screen before running file

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
  #(maybe advanced setup rules?)

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

  #IF GAME IS NOT OVER, ROLL THE DICE
  for i in range(playerNum):
    players[i].outputPlayerInfo()
    players[i].canRoll = 1
    players[i].timesMovedThisTurn=0
    playerChoice(i, players, tiles)
    #TODO maybe get the code to try another command if the player is being dumb
