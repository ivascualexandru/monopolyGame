def playerChoice(i, players, tiles):
    print("Player " + str(i+1) + "'s turn")
    playerDecision = input("Roll / Build / End:")
    if (playerDecision == "Roll"):
        players[i].moveSpaces(players[i].rollDice())
        print("Player " + str(i) +" arrived at " + tiles[players[i].position].name)
        if (tiles[players[i].position].ownedBy == 0): #IF TILE ISN'T ALREADY OWNED BY ANYONE IN THE GAME
            print("It appears the tile you landed on isn't owned by anyone, and costs " + str(tiles[players[i].position].price))
            buy = input("Do you want to buy it? [Y/N] (Your money: " + str(players[i].money) + ").")
            if (buy == "Y"):
                players[i].buyTile(tiles[players[i].position])
            elif (buy == "N"):
                pass
            else:
                raise ValueError('Answer not Y or N')
    elif (playerDecision == "End"):
      pass
    else:
      raise ValueError('Answer not Roll or End')