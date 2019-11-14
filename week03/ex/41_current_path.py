import os

def current_path():
	""" Get the current path of the executed program
		Args: No
		Return: The current path of the working project
	"""
	file_directory = os.getcwd()#getcwd stand for get current working directory

	return file_directory