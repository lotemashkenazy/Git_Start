import random


def choose_word():
    list_words = ['travel', 'person', 'strong', 'street', 'turtle', 'purple', 'orange',
                  'potato', 'august', 'better', 'breath', 'market', 'repair', 'school',
                  'colony', 'online', 'carrot', 'rabbit', 'doctor']
    word = random.choice(list_words)
    #word = list_words[random_word]
    return word

def right_guess(guess, word, correct_letters_print):
    print("you are right!")
    for i in range(len(word)):
        if word[i] == guess:
            correct_letters_print[i] = guess
    print(''.join(correct_letters_print))

def start_welcome(name, correct_letters_print):
    print()
    print("Hello", name, ". Please guess your next letter”")
    print("your word:", correct_letters_print)

def illegal_guese(guess):
    while len(guess) != 1 or guess.isalpha() == False:
        print("your guess is illegal, try again")
        guess = input("your guess:")

def guesed_already(guess, all_guessed_player):
    while guess in all_guessed_player:              # check if he didn't guess this letter already
        print("you guessed this letter already... try again")
        guess = input("your guess:")


def during_game(name, word, all_guessed_player, correct_letters_print):
    start_welcome(name, correct_letters_print)

    if ' _' in correct_letters_print:             #if he didnt guess all the letters yet
        win = 0
        guess = input("your guess:")
        if len(guess) == 1 and guess.isalpha():       #check if the guess is legal
            if guess in all_guessed_player:           #check if he didnt guess this letter already
                guesed_already(guess, all_guessed_player)
            else:
                all_guessed_player += guess
                if guess in word:                   #for good guess!!!(:
                    right_guess(guess, word, correct_letters_print)
                else:
                    print(guess, "not in your word... keep trying!")
        else:
            illegal_guese(guess)
            #print("your guess is illegal")
        if ' _' not in correct_letters_print:
            win = 1
    else:
        win = 1
        print("you win!!! well done (;")

    return win


name_player1 = input("Hi! please enter your name:)")
name_player2 = input("Hi! please enter your name:)")
word_player1 = choose_word()
word_player2 = choose_word()

all_guessed_player1 = []
correct_letters_print1 = [" _"] * len(word_player1)

all_guessed_player2 = []
correct_letters_print2 = [" _"] * len(word_player1)

while True:

    if during_game(name_player1, word_player1, all_guessed_player1, correct_letters_print1) == 1:
        print("player 1 win!!!!!!!!!")
        break
    if during_game(name_player2, word_player2, all_guessed_player2, correct_letters_print2) == 1:
        print("player 2 win!!!!!!!!!")
        break
