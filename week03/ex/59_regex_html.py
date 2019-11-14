import re

def regex_html(html_str):
	''' Remove the html style keep only the normal text
		Arg: Simple html code
		Return: New string only text with out any html syntax
	'''
	res_str = ""
	pattern = r"\<.*?\>"

	res_str = re.sub(pattern, "", html_str)

	return res_str


# if regex_html("<html lang = 'pl' ><body> content of body </body> ... </html>") == " content of body  ... ":
# 	print("OK")
# else:
# 	print("KO")
# print(regex_html("<h1>hello</h1> <p>hello</p>"))
# print(regex_html("<<><>>><>"))

