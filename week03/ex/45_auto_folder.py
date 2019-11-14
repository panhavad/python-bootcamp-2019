import os, shutil

def auto_folder(foldername_list):
	''' Create nultiple folder with the name given in the list
	    Arg: List of string represent folder names
	    Return: 1, 0 on state of operation
	'''
	res = 0
	for foldername in foldername_list:
		if duplicate_checker(foldername):
			res = 1
			if os.path.exists(foldername):
				shutil.rmtree(foldername)
			os.makedirs(foldername)
		else:
			continue

	return res


#this function is use to help auto_folder to be more readable
def duplicate_checker(foldername):
	if os.path.exists(foldername):
		option = input(f"Are you sure you want to replace {foldername}? [Y/N]")
		if option.lower() == "y":
			return True
		elif option.lower() == "n":
			return False
		else:
			print("Invalid Option")
			return duplicate_checker(foldername)
	else:
		return True