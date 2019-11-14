import os, sys

def current_folder():
	current_path = os.getcwd()#getcwd() function to get the current woring directory
	everything_inside = os.walk(current_path)#walk function to get walk through everything is the path
	res_list = list()
	this_file = os.path.basename(sys.argv[0])#this file name
	#without the .path.basename is return ./filename
	
	FOLDER_TYPE = "Folder"
	FILE_TYPE = "File"

	for path, folder, file in everything_inside:
		folder_list = sorted(folder)
		file_list = sorted(file)
		
		for folder_name in folder_list:
			res_list.append((folder_name, FOLDER_TYPE))

		for file_name in file_list:
			if file_name not in this_file:
				res_list.append((file_name, FILE_TYPE))
		#break because want to do only one loop
		break

	return res_list