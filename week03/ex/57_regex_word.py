import re

def regex_word(max_len, simple_str):
	''' Remove word from string base on the given len
		Arg: len of the word and to remove
			string to be operating on
		Return: the existing string
	'''
	res_str = ""
	if max_len > 0:
		pattern = r"(\b\w{1," + str(max_len) + r"}\s?\b)"
		res_str = re.sub(pattern, "", simple_str)

	return res_str

# print(regex_word(3, "My name is Kevad"))
# print(regex_word(5, "How are you today?"))
# print(regex_word(2, "Is it a cat or is it a dog?"))
# print(regex_word(0, "Is it a cat or is it a dog?"))
# print(regex_word(-2, "Is it a cat or is it a dog?"))


