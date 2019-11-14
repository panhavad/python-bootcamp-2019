input_str = input("Enter a string: ")
interval = 0
final_str = ""

#get each element of the string and assign to final_string reversly
while interval < len(input_str):
	final_str += input_str[-interval - 1]
	interval += 1

print(final_str)