final_str = ""

while True:
	input_str = input("Enter a string: ")
	#by using lower here is to make our program is not case sensitive
	if input_str.lower() != "generate":
		final_str += "<p>" + input_str + "</p>\n"
	else:
		break

print(final_str)