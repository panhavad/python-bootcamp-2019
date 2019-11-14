import os, shutil

def delete_file(filename):
	''' Delete the file of the given name
		Arg: name of the file want to delete
		Return: 1, 0 base on operation
	'''
	if os.path.exists(filename):
		option = input(f"Are you sure you want to delete {filename}? [Y/N]")
		if option.lower() == "y":
			try:
				os.remove(filename)
			except Exception as e:
				shutil.rmtree(filename)
			return 1
		elif option.lower() == "n":
			return 0
		else:
			print("Invalid Option")
			return delete_file(filename)
	else:
		return 0