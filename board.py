class Tile:
  name = "N\A"
  price = 99999
  ownedBy = 9
  _counter = 0

  def __init__(self, name, price, ownedBy, noOfHouses, _counter):
    self.name = name
    self.price = price
    self.tile = 0
    Tile._counter += 1
    self.tileNo = Tile._counter
    print("Tile created with name " + self.name + " and price " + str(self.price) + " at position " + str(_counter))

pricesForTiles = {
  #TODO
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
