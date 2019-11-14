total = 0

while True:
	input_num = (input("Enter a number: "))
	if input_num.isdigit() or input_num.lstrip("-").isdigit():
	#lstrip function use to trim out the character in the parameter
		input_num = int(input_num)
		total += input_num
		print("TOTAL:", total)
	else:
		if input_num == "":
			print("TOTAL:", total)
		elif input_num.lower() == "exit":
			exit()#function to terminate the program
