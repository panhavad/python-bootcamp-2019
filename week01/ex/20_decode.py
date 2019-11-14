""" 
	HowTo: 
		- Detecting the alphabet only
		- Converting alphabet to ascii value 
		- Minus that ascii value by 13 if reach maximum then go back to the start

"""

input_str = input("Enter your secret message: ")
final_string = ""

if len(input_str) > 0: 
	for element in input_str:
		element_ascii_val = ord(element)
		#detecting lowercase
		if element_ascii_val >= 97 and element_ascii_val <= 122:
			if element_ascii_val - 13 < 97:
				#calculation when reach "a"
				final_string += chr(((element_ascii_val - 13) + 122) - 96)
			else:
				final_string += chr(element_ascii_val - 13)
		#detecting uppercase
		elif element_ascii_val >= 65 and element_ascii_val <= 90:
			if element_ascii_val - 13 < 65:
				#calculation when reach "A"
				final_string += chr((((element_ascii_val - 13) + 90)) - 64)
			else:
				final_string += chr(element_ascii_val - 13)
		else:
			final_string += element
else:
	print("Nothing to decode.")
#display the final output
print(final_string)
