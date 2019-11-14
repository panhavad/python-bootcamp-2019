import re

def regex_par(simple_str):
	''' Remove other the complete parenthesis
		Arg: String to be operate
		Return: New string without any parenthesis
	'''
	res_str = ""
	pattern = r"\s?\(.+?\)"
	
	res_str = re.sub(pattern, "", simple_str)
	
	return res_str

# if regex_par("((not ok)) )ok( )))(not_ok)(((ok") == ") )ok))(((ok":
# 	print("OK")
# else:
# 	print("KO")

# if regex_par("(hello) Welcome to KIT (Kirirom Institute of Technology)!") == " Welcome to KIT!":
# 	print("OK")
# else:
# 	print("KO")

# if regex_par("") == "":
# 	print("OK")
# else:
# 	print("KO")



