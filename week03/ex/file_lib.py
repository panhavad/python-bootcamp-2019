import os, shutil, sys

class FileLib():
	
	def current_folder(self):
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
			break

		return res_list


	def current_path(self):
		"""
		Args: No
		Return: The current path of the working project
		"""
		file_directory = os.getcwd()
		
		return file_directory

	
	def read(self, filename):
		content = ''
		try:
			file = open(filename, 'r')#open filename with read mode
			content = file.read()#read the content
			file.close()#close the file
		except Exception as e:
			print("Invalid FILENAME")
		
		return content


	def write(self, filename, content):
		if self.duplicate_checker(filename):
			with open(filename, 'w+') as file:
				file.write(content)
			return 1
		else:
			return 0

		
	def append(self, filename, content):
		try:
			with open(filename, 'a') as file:
				file.write(content)
				return 1
		except Exception as e:
			return 0


	def remove(self, filename):
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


	def create_folder(self, folder_list):
		res = 0
		
		for foldername in folder_list:
			if self.duplicate_checker(foldername):
				res = 1
				if os.path.exists(foldername):
					shutil.rmtree(foldername)
				os.makedirs(foldername)
			else:
				continue

		return res


	#this function is to assist some other function
	def duplicate_checker(self, filename):
		if os.path.exists(filename):
			option = input(f"Are you sure you want to delete {filename}? [Y/N]")
			if option.lower() == "y":
				return True
			elif option.lower() == "n":
				return False
			else:
				print("Invalid Option")
				return self.duplicate_checker(filename)
		else:
			return True