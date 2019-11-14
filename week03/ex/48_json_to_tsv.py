import json, os
#using json.load our json formate will be list of dictionary

def json_to_tsv(jsonfile, tsvfile):
	''' Coverte json file to tsv file
		Arg: jsonfile name
			tsvfile name
		Return: 1 on success operation
				0 on fail operation
	'''
	jsonfile, tsvfile = file_checker(jsonfile, tsvfile)
	try:
		with open(jsonfile, 'r') as json_file:
			with open(tsvfile, 'w+') as tsv_file:
				json_data = json.load(json_file)
				json_keys = list(json_data[0].keys())
				
				for key in json_keys:
					if key != json_keys[-1]:
						tsv_file.write(f"{key}\t")
					else:#prevent from give empty value to next column
						tsv_file.write(f"{key}\n")	
				
				for each_dict in json_data:
					json_values = list(each_dict.values())
					
					for each_value in json_values:
						if each_value != json_values[-1]:
							tsv_file.write(f"{each_value}\t")
						else:#prevent from give empty value to next column
							tsv_file.write(f"{each_value}\n")

		return 1
	except FileNotFoundError as e:
		return 0

#check and correct bad file name
def file_checker(jsonfile_name, tsvfile_name):
	json_extension, tsv_extension = os.path.splitext(jsonfile_name)[-1], os.path.splitext(tsvfile_name)[-1]

	if not os.path.exists(jsonfile_name):
		if json_extension is '':
			jsonfile_name += ".json"
	else:
		jsonfile_name = jsonfile_name


	if tsv_extension is '':
		tsvfile_name += ".tsv"
	else:
		tsvfile_name = tsvfile_name

	return jsonfile_name, tsvfile_name