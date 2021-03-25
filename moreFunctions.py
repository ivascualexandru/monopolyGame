def playerChoice(i, players, tiles):
    print("Player " + str(i+1) + "'s turn\nPlease select your choice:")
    playerOptions = []
    if (players[i].canRoll == 1):
        playerOptions.append("Roll")    
        playerOptions.append("Build")
    else:
        playerOptions.append("Build")
        playerOptions.append("End")
    for i in range(len(playerOptions)):
        print(playerOptions[i], end=' / ')
    playerDecision = input("\n")
    if (playerDecision in playerOptions):
        if (playerDecision == "Roll"):
            if (players[i].canRoll == 1):
                players[i].moveSpaces(players[i].rollDice(), players, tiles)
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
            elif (players[i].canRoll == 0):
                print("Sorry! You can't roll. Please pick either Build (TODO) or End.")


        elif (playerDecision == "End"):
            players[i].canRoll = 1
            players[i].timesMovedThisTurn = 0
            return 0

        else:
            raise ValueError('Answer not Roll, Build (TODO) or End')
    else:
        print("Whoops! Wrong choice. Try again.")
    return playerChoice(i, players, tiles)