from moreFunctions import playerChoice
import random

class Player:

  _counter = 0
  timesMovedThisTurn = 0
  canRoll = 1

  def __init__(self, money, name):
    self.money = money
    self.name = name
    self.position = 0
    self.playerNo = Player._counter
    Player._counter += 1
    print("Player created with name " + self.name + " and money " + str(self.money) + " at tile " + str(self.position))
  
  def __del__(self):
    self._counter-=1

  def rollDice(self):
    #TODO maybe if they roll doubles thrice in a row have them land in jail,
    #money -= 200 or roll doubles again to get out (automatically get out after 3 turns)

    randomNum1 = random.randint(1,6)
    randomNum2 = random.randint(1,6)
    print("Rolled a " + str(randomNum1) + " and a " + str(randomNum2) + "!")
    self.canRoll = 0
    if (randomNum1 is randomNum2):
      print("Doubles!")
      self.canRoll = 1
      self.timesMovedThisTurn+=1
    return randomNum1*10+randomNum2


  def moveSpaces(self, dice, players, tiles):
    die1 = int(dice/10)
    die2 = dice%10
    if(self.timesMovedThisTurn is 3):
      print("3 Rolls in a single turn? You're going to jail, mister!")
      #TODO goToJail
    else:
      self.position = self.position + die1 + die2
      print("Player " + str(self.playerNo) +" arrived at " + tiles[players[self.playerNo].position].name)
      if (tiles[players[self.playerNo].position].ownedBy == 0): #IF TILE ISN'T ALREADY OWNED BY ANYONE IN THE GAME
        print("It appears the tile you landed on isn't owned by anyone, and costs " + str(tiles[players[self.playerNo].position].price))
      buy = input("Do you want to buy it? [Y/N] (Your money: " + str(players[self.playerNo].money) + ").")
      if (buy == "Y"):
          players[self.playerNo].buyTile(tiles[players[self.playerNo].position])
      elif (buy == "N"):
          pass
      else:
          raise ValueError('Answer not Y or N')
      self.timesMovedThisTurn+=1
      if (die1 is die2):
        #prompt player to Roll again
        playerChoice(self.playerNo, players, tiles)
        #TODO
      print("Player " + self.name +" is now at " + str(self.position))
      #if tile is already owned
        #look up price based on number of houses on that tile (make separate dictionary/list/whatever)
        #and pay the owner the price
        #and output the players' money
      if (self.position > 39):
        self.position = self.position - 40
        self.money+=200
        print("Player " + self.name +" is now at " + str(self.position))

  def outputPlayerInfo(self):
    print("Player " + self.name)
    print("Name: " + self.name + "     Money: " + str(self.money))
    print("Position: " + str(self.position))

  def buyTile(self, tileCurrentlyOn):
    if (self.money >= tileCurrentlyOn.price and tileCurrentlyOn.ownedBy is 0):
      self.money -= tileCurrentlyOn.price
      tileCurrentlyOn.ownedBy = self.playerNo
      print("Tile number " + str(tileCurrentlyOn.position) + " is now owned by player " + str(self.name) + ".")
    else:
      print("Whoops! You don't have any money.")
