import numpy

card1 = int(input("enter card 1:"))
card2 = int(input("enter card 2:"))
card3 = int(input("enter card 3:"))


if (card1 == card2) or (card1 == card3) or (card2 == card3):
    print("draw")
elif (card1 > card2) and (card1 > card3):
    if card2+card3 == card1:
        if card2 < card3:
            print("player 2 is the winner!")
        else:
            print("player 3 is the winner!")
    else:
        print("player 1 is the winner!")

elif (card2 > card1) and (card2 > card3):
    if card1 + card3 == card2:
        if card1 < card3:
            print("player 1 is the winner!")
        else:
            print("player 3 is the winner!")
    else:
        print("player 2 is the winner!")

elif (card3 > card1) and (card3 > card2):
    if card1 + card2 == card3:
        if card1 < card2:
            print("player 1 is the winner!")
        else:
            print("player 2 is the winner!")
    else:
        print("player 3 is the winner!")