import random

winner = ""
count_of_guesses = 1
min_guesses = 0
num_of_players = int(input("enter the number of players:"))
for i in range(1, num_of_players + 1):
	value = random.randint(0, 100)
	print(value)
	count_of_guesses = 1
	guess = int(input("Player X, please type your guess:"))
	while guess != value:
		if guess > value:
			guess = int(input("Too high. Try again:"))
			count_of_guesses += 1
		elif guess < value:
			guess = int(input("Too low. Try again:"))
			count_of_guesses += 1
	if min_guesses == 0:
		min_guesses = count_of_guesses
		winner = "The winner is " + str(i)
	if count_of_guesses < min_guesses:
		min_guesses = count_of_guesses
		winner = "The winner is " + str(i)
	if (count_of_guesses == min_guesses) and (i != 1):
		#winner += (" and player " + str(i))
		winner = "The winners are " + winner[-1] + " and player " + str(i)

	print("Well done! You're right in", count_of_guesses, "guesses")
print(winner)
