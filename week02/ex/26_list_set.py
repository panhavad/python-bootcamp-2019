def list_set(list_values):
	"""Refine the list and keep only unique value

    Args:
      any list of string or number
    Returns:
      list of unique value

    This is not a good performance
	# set_values = set()
	# for list_element in list_values:
	# 	set_values.add(list_element)
	# list_values.clear()#clear the list and reuse at the end
	# for set_element in set_values:
	# 	list_values.append(set_element)
	# print(list_values)
	"""

	#Better using this :)
	list_values = set(list_values)
	list_values = list(list_values)
	print(list_values)

	return list_values

#START HERE
# list_set(['456', '123', '789', '123', '123', '123', 'abc', 'abc', 'def'])

#CALLING
# print(list_set(['456', '123', '789', '123', '123', '123', 'abc', 'abc', 'def']))