import board

class Player:

  _counter = 0

  def __init__(self, money, name, _counter):
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
    #print("Passed args: Money is " + str(self.money) + ", price is " + str(tileCurrentlyOn.price) + ", name is " + tileCurrentlyOn.name, "position is " + str(tileCurrentlyOn._counter))
    if (self.money >= tileCurrentlyOn.price):
      self.money -= tileCurrentlyOn.price
      tileCurrentlyOn.ownedBy = self._counter
      print("Tile number " + str(tileCurrentlyOn._counter) + " is now owned by player " + str(self.name) + ".")
    else:
      print("Whoops! You don't have any money.")

    '''
          if (players[i].money >= tiles[players[i].position].price):
            print("Placeholder to buy Tile")
            players[i].buyTile(tiles[players[i].position])
          else:
            print("Whoops! You don't have any money.")
          players[i].money -= tiles[players[i].position].price
          tiles[players[i].position].ownedBy = i
          print("Tile " + tiles[players[i].position].name + "has been bought by player " + str(i))
    '''

  #TODO fix the buyTile function (line 18, 'Tile' object is not subscriptable)