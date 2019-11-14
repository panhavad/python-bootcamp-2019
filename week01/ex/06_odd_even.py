while True:
	number = (input("Enter a number:\n"))
	
	if number.isdigit():
		number = int(number)
		if number % 2 == 0:
			print(number, "is EVEN")
		else:
			print(number, "is ODD")
	else:
		if number.lower() == "exit":
			exit()#function to terminate the program
		else:
			print(number, "is not a valid number.")