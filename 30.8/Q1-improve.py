import random

players = []
num_of_players = int(input("Enter the number of players:"))


i = 0
while len(players) < num_of_players:
    players.append(input("Enter player"))
    i += 1
print("The players:", players)

#chair = random.randint(0, len(players) - 1)
#standing_player = players[chair]
#players.remove(standing_player)

while len(players) > 1:                              # 0 INSTEAD OF 1
    chair = random.randint(0, len(players) - 1)      # HERE INSTEAD OF BEFORE THE WHILE
    standing_player = players[chair]
    players.remove(standing_player)

    print()
    music = input("is the music still playing? Y/N")
    if music == "Y":
        chair = random.randint(0, len(players) - 1)
        standing_player, players[chair] = players[chair], standing_player

    elif music == "N":
        if len(players) == 1:
            print("The player that left:", standing_player)
            print("The winner is:", players, "!!!!!!(:")
            #break

        else:
            print("The players:", players)
            print("The player that left:", standing_player)

            #chair = random.randint(0, len(players) - 1)
            #standing_player = players[chair]
            #players.remove(standing_player)

    else:
        print("The answer is illegal, please enter Y/N")