import re

def regex_alpha(simple_str):
	''' Check the given string contain only a-z A-Z 0-9
		Arg: simple string value
		Return: True, False
	'''
	pattern = re.compile(r"[^a-zA-Z0-9]")
	res = pattern.findall(simple_str)
	if len(simple_str) > 0:
		if len(res) > 0:
			return False
		else:
			return True
	else:
		return False

# print(regex_alpha("abc123"))
# print(regex_alpha("asdkcnaejiwoecamweo234120934190238"))
# print(regex_alpha("asdkcnaejiwoecamweo2 34120934190 238"))
# print(regex_alpha("asdkcnaejiJASDAJDwoecamweo234120934190238"))
# print(regex_alpha("asdkcnaejiJASDAJDwoecamweo234120934(*&!@(190238"))
# print(regex_alpha("ABC123"))
# print(regex_alpha("ABC12 3!*"))
# print(regex_alpha("ABC123!"))
# print(regex_alpha(""))


