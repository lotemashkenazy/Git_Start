card1_player1 = int(input("please enter your card (1-13):"))
card1_player2 = int(input("please enter your card (1-13):"))
if card1_player1 == 1:
    card1_player1 += 14
if card1_player2 == 1:
    card1_player2 += 14

if card1_player1 > card1_player2:
    print("player 1 is the winner")
elif card1_player2 > card1_player1:
    print("player 2 is the winner")
elif card1_player1 == card1_player2:
    card2_player1 = int(input("please enter your second card (1-13):"))
    card2_player2 = int(input("please enter your card second (1-13):"))
    if card2_player1 == card2_player2:
        print("draw")
    elif card2_player1 == 1:
        print("player 1 is the winner")
    elif card2_player2 == 1:
        print("player 2 is the winner")
    elif (card2_player1 > card2_player2) and card2_player1 - card2_player2 <= 2:
        print("player 1 is the winner")
    elif (card2_player2 > card2_player1) and card2_player2 - card2_player1 <= 2:
        print("player 2 is the winner")
    else:
        print("draw")