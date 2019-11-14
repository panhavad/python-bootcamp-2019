#import all module in random class
from random import *

try:
	input_num = int(input("Enter a number: "))

	while input_num > 0:
		'''
			randrange(a, b): the param b will not include in the random numbers
				print(randrange(1, 101))

			For the currect exercise using randint might be give more sense
				because randint(a,b) the random number is include the b value too

		'''
		print(randint(1, 100))
		input_num -= 1

except Exception as e:
#handle the exception when the input is not int or negative int
	print("Warning: Invalid input!")
	