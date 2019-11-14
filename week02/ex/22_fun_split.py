def fun_split(string):
	"""Split string base on SPACE

    Args:
      any string
    Returns:
      list of each part that splited by space
    """
	if len(string) > 0:
		str_list = list(string.split(" ")) 
	else:
		str_list = list()

	print(str_list)

	return str_list

#START HERE
# fun_split("Hello! It’s me again!")
# fun_split("")

#CALLING
print(fun_split("Hello! It’s me again!"))

	
