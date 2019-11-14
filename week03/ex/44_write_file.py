import os

def write_file(filename, content):
	''' Write content to the given name of file
		Arg: name of the file want to write
			content that want to write
		Return: 1 for success
				0 for not success
	'''
	if duplicate_checker(filename):
		try:
			with open(filename, 'w+') as file:#w+ is to create file if not exist
				file.write(content)
				return 1
		except Exception as e:#handle in case there are some special char in file name
			return 0
	else:
		return 0

#this function is to help the write_file more readable
def duplicate_checker(filename):
	if os.path.exists(filename):
		option = input(f"Are you sure you want to replace {filename}? [Y/N]")
		if option.lower() == "y":
			return True
		elif option.lower() == "n":
			return False
		else:
			print("Invalid Option")
			return duplicate_checker(filename)
	else:
		return True