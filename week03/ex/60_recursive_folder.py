import os, sys

def recursive_folder(folder_path):
	''' Get the file path in all of the root from the given path
		Arg: Path as a string
		Return: List of path of file in each sub-directory
	'''
	
	this_file = os.path.basename(sys.argv[0])#this file name
	scan_res = os.walk(folder_path)
	res_list = list()

	for root, folders, files in sorted(scan_res):
		
		if len(files) > 0:
			
			for file in files:
				if file != this_file:
					res_list.append(os.path.join(root, file))

	return res_list

print(recursive_folder("C:\\Users\\panha\\Desktop\\main"))
