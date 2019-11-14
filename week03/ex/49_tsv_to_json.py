import json, os, csv
#using json.load our json formate will be list of dictionary

def json_to_tsv(tsvfile, jsonfile):
	tsvfile, jsonfile = file_checker(tsvfile, jsonfile)
	
	try:
		with open(tsvfile, 'r') as tsv_file:
			with open(jsonfile, 'w+') as json_file:
				res_json = list()
				tsv_content = list(csv.reader(tsv_file, delimiter="\t"))
				json_key = tsv_content[0]
				json_value = tsv_content[1:len(tsv_content)]
				
				for each_list in json_value:
					interval = 0
					res_dict = dict()
					
					for each_value in each_list:
						res_dict[json_key[interval]] = each_value
						interval += 1
					
					res_json.append(res_dict)
				
				formated_json = json.dumps(res_json, indent=4)
				json_file.write(formated_json)
		
		return 1
	
	except FileNotFoundError as e:
		return 0

#check and handle to bad name file input
def file_checker(tsvfile_name, jsonfile_name):
	json_extension, tsv_extension = os.path.splitext(jsonfile_name)[-1], os.path.splitext(tsvfile_name)[-1]
	
	if tsv_extension is '':
		tsvfile_name += ".tsv"
	else:
		tsvfile_name = tsvfile_name


	if json_extension is '':
		jsonfile_name += ".json"
	else:
		jsonfile_name = jsonfile_name

	return tsvfile_name, jsonfile_name