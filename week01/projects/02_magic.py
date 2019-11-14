"""
	
	STEPS:	
		- Welcome message
		- player input (3 times) with message
			- Display state message if not correct (Until 3rd time)
		- Play again message if correct (Y/N)
			- Y recall funtion
			- N display Good bye message
			- Ask again with other message if not N or Y
		- Correct first time display Congrate message

	WARNING:
		- 
	
	FORBIDEN:
		- No misspelling
	
	RECOMMENDED:
		- Using CONSTANT
	
	TESTED:
		- Any string for name    OK
		- Lower number    OK
		- Higher number    OK
		- Name input
			- No Name    OK
			- Space in name   OK
			- Name number    OK
			- Name with space alpha and number    OK
			- Special character name    OK
		- Guess number input    OK
			- Empty    OK
			- Character    OK
			- Negative number    OK
			- BLANK    OK
			- 
		- Play again    OK
			- Y    OK
			- N    OK
			- 1234    OK
			- )*^^&$^$    OK
			- LJNSLANSDKNaklsdklasn    OK
			- BLANK    OK

"""

from random import *

WELCOME_MESSAGE = "Hello, what is your name?\n"
SPECIAL_MESSAGE = "You won in 1 turn only, that's amazing!"
REPLAY_MESSAGE = "Do you want to play again? [Y/N]\n"
MAX_CHANCE = 3
RANDOM_MIN = 1
RANDOM_MAX = 100

def intro_game():
	player_name = input(WELCOME_MESSAGE)
	#player_name.replace(' ', '').isalpha() to handle the name with space "Duk Panhavad"
	#name only alphabet and space is allow
	if len(player_name) > 0 and player_name.replace(' ', '').isalpha():
		start_game(player_name, 0, True)
	else:
		print("Invalid input!")
		intro_game()

def random_number():
	return randint(RANDOM_MIN, RANDOM_MAX)


def start_game(player_name, actual_number, new_game_flag):
	"""

		new_game_flag is to make this game fair :)

		new_game_flag handle 2 conditions: 
			- when invalid input game repeat with 
				same previous number to be guess
			- when game end and start fresh with 
				same or new user game will random new number


	"""
	if new_game_flag:
		actual_number = random_number()
	else:
		actual_number = actual_number
	#RECOMMENDED: uncomment this when testing
	# print("---", actual_number, "actual_number")
	try:
		guess_number = int(input(f"Well {player_name}, try to guess the number I have in mind!\n"))
	except Exception as e:
		invalid_checker(player_name, actual_number)
	if guess_number < 0:
		invalid_checker(player_name, actual_number)

	guess_count = 1
	result_checker(guess_number, player_name, actual_number, guess_count)

def result_checker(guess_number, player_name, actual_number, guess_count):
	#RECOMMENDED: uncomment this when testing
	# print("---", guess_count, "guess_count")
	if guess_count <= MAX_CHANCE:
		if guess_number == actual_number:
			if guess_count == 1:
				print(SPECIAL_MESSAGE)
			else:
				print(f"It took you {guess_count} turns to guess my number which was {actual_number}!")
			replay_display(player_name, actual_number)
		elif guess_number > actual_number:
			high_low_checker(guess_number, player_name, actual_number, guess_count, "high")
		else:
			high_low_checker(guess_number, player_name, actual_number, guess_count, "low")
	else:
		replay_display(player_name, actual_number)

def high_low_checker(guess_number, player_name, actual_number, guess_count, guess_state):
	if guess_count != MAX_CHANCE:
		try:
			guess_number = int(input(f"Too {guess_state}, try again!\n"))
		except Exception as e:
			print("Invalid input!")
		finally:
			guess_count += 1
			result_checker(guess_number, player_name, actual_number, guess_count)
	else:
		replay_display(player_name, actual_number)

def invalid_checker(player_name, actual_number):
	print("Invalid input! Try again!")
	start_game(player_name, actual_number, False)


def replay_display(player_name, actual_number):
	replay_flag = input(REPLAY_MESSAGE)
	if replay_flag.lower() == "y":
		start_game(player_name, actual_number, True)
	elif replay_flag.lower() == "n":
		print(f"Ok, bye {player_name}! See you later!")
		exit()
	else:
		print("Sorry, I did not understand. Let me repeat:")
		replay_display(player_name, actual_number)

#START HERE
intro_game()