times = input("Enter a number:\n")
if times is not '':
	times = int(times)
	while times > 0:
		print("Hello World!")
		times -= 1
else:
	print("Nothing to display")
