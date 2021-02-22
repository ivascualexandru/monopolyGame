class Tile:
  name = "N\A"
  price = 99999
  ownedBy = 0
  _counter = 0

  def __init__(self, name, price, ownedBy, noOfHouses, _counter):
    self.name = name
    self.price = price
    #self.tile = Tile._counter
    Tile._counter += 1
    self.tileNo = Tile._counter
    print("Tile created with name " + self.name + " and price " + str(self.price) + " at position " + str(_counter))

  def getPrice(self):
    return pricesForTiles[self._counter]

pricesForTiles = {
  0: 999999,
  1: 60,
  2: 999999,
  3: 60,
  4: 999999,
  5: 200,
  6: 100,
  7: 999999,
  8: 100,
  9: 120,
  10: 999999,
  11: 140,
  12: 150,
  13: 140,
  14: 160,
  15: 200,
  16: 180,
  17: 999999,
  18: 180,
  19: 200,
  20: 999999,
  21: 220,
  22: 999999,
  23: 220,
  24: 240,
  25: 200,
  26: 260,
  27: 260,
  28: 150,
  29: 280,
  30: 999999,
  31: 300,
  32: 300,
  33: 999999,
  34: 320,
  35: 200,
  36: 999999,
  37: 350,
  38: 999999,
  39: 400
}

namesForTiles = {
  0: "Start",
  1: "Old Kent Road",
  2: "Community Chest",
  3: "Whitechapel Road",
  4: "Income Tax",
  5: "Kings Cross Station",
  6: "The Angel, Inslington",
  7: "Chance",
  8: "Euston Road",
  9: "Pentonville Road",
  10: "In Jail / Just Visiting", #TODO: Revisit this and make it one way or the other
  11: "Pall Mall",
  12: "Electric Company",
  13: "WhiteHall",
  14: "Northumrl'd Avenue",
  15: "Marylebone Station",
  16: "Bow Street",
  17: "Community Chest",
  18: "Marlborough Street",
  19: "Vine Street",
  20: "Free Parking",
  21: "Strand",
  22: "Chance",
  23: "Fleet Street",
  24: "Trafalgar Square",
  25: "Fenchurch St. Station",
  26: "Leicester Square",
  27: "Coventry Street",
  28: "Water Works",
  29: "Piccadilly",
  30: "Go To Jail",
  31: "Regent Street",
  32: "Oxford Street",
  33: "Community Chest",
  34: "Bond Street",
  35: "Liverpool St. Station",
  36: "Chance",
  37: "Park Lane",
  38: "Super Tax",
  39: "Mayfair"
}
