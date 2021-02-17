class Player:
  def __init__(self, money, name):
    self.money = money
    self.name = name
    self.tile = 0
    print("Player created with name " + self.name + " and money " + str(self.money) + " at tile " + str(self.tile))
  
  def moveSpaces(self, spacesToMove):
    self.tile = self.tile + spacesToMove
    if (self.tile > 39):
      self.tile = self.tile - 40
    print("Player " + self.name +" is now at " + str(self.tile))

    '''
    TODO: DO THE BOARD LOGIC AND MAYBE HAVE IT REDUCE THE PLAYERS' MONEY
    '''
