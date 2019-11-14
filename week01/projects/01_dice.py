"""
	
	STEPS:	
		- Welcome message
		- User input the number of dice to use (1 - 8)
		- Display each dice value and sum value
	
	WARNING:
		- One dice contain 6 value (1 to 6)
		- Nothing is pass -> display warning -> ask for input with massage again
		- Input allow only 1 to 8
	
	FORBIDEN:
		- Using array
	
	RECOMMENDED:
		- Using CONSTANT
	
	TESTED:
		- Input 1    OK
		- Input 2 to 8    OK
		- Input greater 8    OK
		- Input characters    OK
		- Input special symbol    OK
		- Input blank    OK
		- Input negative value    OK
		- Input decimal number    OK

"""

from random import *

#define constant
INTRO_MESSAGE = "Welcome to the dices game!"
USAGE_MESSAGE = "USAGE: The number must be between 1 and 8"
INTRUCTION_MESSAGE = "Enter the number of dices you want to roll: "
#number of dice
MAX_OF_DICES = 8
MIN_OF_DICES = 1
#value in one dice
MIN_DICE_VALUE = 1
MAX_DICE_VALUE = 6


def start_game():
	
	#variable declareation
	final_dices_res = 0
	dice_number = 1 #assign value 1 give more sense then 0
	dice_one_flag = False

	#handle all invalid input from user
	try:
		
		amount_dice = int(input(INTRUCTION_MESSAGE))
		
		#amount_dice > 0 is to prevent negative value
		if amount_dice <= MAX_OF_DICES and amount_dice >= MIN_OF_DICES:

			while dice_number <= amount_dice:

				#randint is allow to random until last number
				dice_current_res = randint(MIN_DICE_VALUE, MAX_DICE_VALUE)
				final_dices_res += dice_current_res
				
				if amount_dice == 1:
					dice_one_flag = True
				else:
					print("Dice", dice_number, ":", dice_current_res)
					dice_one_flag = False
				
				dice_number += 1

			display_final(dice_one_flag, final_dices_res)

		else:

			raise
			
	except Exception as e:
		
		print(USAGE_MESSAGE)
		start_game()


def display_final(dice_one_flag, final_dices_res):
	if dice_one_flag:
		print("RESULT:", final_dices_res)
	else:
		print("==========\n" +
				"RESULT:", str(final_dices_res) +
					"\n==========")

#START HERE
print(INTRO_MESSAGE)
start_game()