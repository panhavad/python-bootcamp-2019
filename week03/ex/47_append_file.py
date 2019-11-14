from datetime import datetime

def append_file(filename):
	''' Write thing inputed string to file with datetime like logging file
		Arg: the file name to be write
		Return: Nothing
	'''
	not_exit = True
	while not_exit:
		with open(filename, 'a') as file:#open file in append mode
			current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
			content_input = input("$: ")
			if content_input.lower() != "exit":
				file.write(f"[{current_datetime}] {content_input}\n")
			else:
				not_exit = False#act like a safety switch
				return exit()