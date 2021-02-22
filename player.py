import board

class Player:

  _counter = 0

  def __init__(self, money, name):
    self.money = money
    self.name = name
    self.position = 0
    Player._counter += 1
    self.playerNo = Player._counter
    print("Player created with name " + self.name + " and money " + str(self.money) + " at tile " + str(self.position))
  
  def moveSpaces(self, spacesToMove):
    self.position = self.position + spacesToMove
    print("Player " + self.name +" is now at " + str(self.position))
    if (self.position > 39):
      self.position = self.position - 40
      print("Player " + self.name +" is now at " + str(self.position))

  def outputPlayerInfo(self):
    print("Player " + self.name)
    print("Name: " + self.name + "     Money: " + str(self.money))
    print("Position: " + str(self.position))

  def buyTile(self, tileCurrentlyOn):
    print("Passed args: Money is " + str(self.money) + ", price is " + str(tileCurrentlyOn.price) + ", name is " + tileCurrentlyOn.name, "position is " + str(tileCurrentlyOn.position))
    if (self.money >= tileCurrentlyOn.price and tileCurrentlyOn.ownedBy is 0):
      self.money -= tileCurrentlyOn.price
      tileCurrentlyOn.ownedBy = self._counter
      print("Tile number " + str(tileCurrentlyOn.position) + " is now owned by player " + str(self.name) + ".")
    else:
      print("Whoops! You don't have any money.")
