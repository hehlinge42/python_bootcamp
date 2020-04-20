from random import randint

to_guess = randint(1, 99)
user_input = 0
nb_attempts = 0

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""")

while user_input != to_guess:
	user_input = input("What's your guess between 1 and 99?\n")
	if user_input == "exit":
		exit()
	try:
		user_input = int(user_input)
	except:
		print("Please provide an integer between 1 and 99")
	else:
		nb_attempts += 1
		if user_input < 1 or user_input > 99:
			print("Please provide an integer between 1 and 99")
		elif user_input < to_guess:
			print("Too low!")
		elif user_input > to_guess:
			print("Too high!")
		elif user_input == to_guess:
			if to_guess == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
			if nb_attempts == 1:
				print("Congratulations! You got it on your first try!")
			elif nb_attempts > 1:
				print("Congratulations, you've got it!\nYou won in %d attempts!" %(nb_attempts))
