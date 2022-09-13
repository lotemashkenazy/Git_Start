#  advanced
import random

YES = "y"
NO = "n"

number_of_participants = int(input("Enter the number of participants:"))
def create_list(number_of_participants):           #create list of the players game_list
    game_list = []
    for i in range(number_of_participants):
        participant = input("Enter participant's name: ")
        game_list.append(participant)
    print("Let the game begin!")
    return game_list

game_list = create_list(number_of_participants)
while len(game_list) > 1:
    standing_participant = game_list.pop()
    is_music = input("Is the music still playing? y/n")
    while is_music != YES and is_music != NO:
        is_music = input("Please enter valid input y/n")

    while is_music == YES:
        random_index = random.randint(0, len(game_list) - 1)
        temp_var = game_list[random_index]
        game_list[random_index] = standing_participant
        standing_participant = temp_var
        is_music = input("Is the music still playing? y/n")
        while is_music != YES and is_music != NO:
            is_music = input("Please enter valid input y/n")
    print(str(standing_participant) + " is out")
    print(game_list)
print("The winner is:" + str(game_list[0]))