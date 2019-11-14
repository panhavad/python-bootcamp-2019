""" 
	lowercase of alphabet ascii value from 97 - 122
	uppercase of alphabet ascii value from 65 - 90

	HowTo: 
		- Use ascii value to detect lowercase or uppercase
		- Plus(lowercase) or Minus(uppercase) 32 of ascii value to change the case of alphabet
		- Allow only ahplabet not all special character to prevent program crashing
	
	Note: I rarely work with ascii value so this note might help me. I try to handle all condition
		that I can think of because I am not familiar with ascii value :)

"""
input_str = input("Enter a string: ")
final_string = ""

if len(input_str) > 0: 
	for element in input_str:
		element_ascii_val = ord(element)
		#detecting lowercase
		if element_ascii_val >= 97 and element_ascii_val <= 122:
			final_string += chr(element_ascii_val - 32)
		#detecting uppercase
		elif element_ascii_val >= 65 and element_ascii_val <= 90:
			final_string += chr(element_ascii_val + 32)
		else:
			final_string += element
else:
	print("Empty")

#display the final output
print(final_string)