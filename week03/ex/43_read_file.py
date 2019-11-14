def read_file(filename):
	''' To read the content in any file
		Arg: filename to be read by the program
		Return: content in the passing file
	'''
	content = ''
	try:
		with open(filename, 'r') as file:#open filename with read mode
			content = file.read()#read the content
	except Exception as e:
		print("Invalid FILENAME")
	
	return content