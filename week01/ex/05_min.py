first_number = int(input("Enter a number:\n"))
second_number = int(input("Enter a second number:\n"))
if first_number < second_number:
	print("Result :", first_number, "<", second_number)
elif second_number < first_number:
	print("Result :", second_number, "<", first_number)
else:
	print("Result :", first_number, "==", second_number)