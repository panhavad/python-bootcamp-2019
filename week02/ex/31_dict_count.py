def dict_count(list_values):
	"""Take list as input and convert to dictionary
		that have Key as the list element and
		occurrences times as value

    Args:
      a list of anything
    Returns:
      a dictionary with proper key and value
    """
	set_values = sorted(set(list_values))
	dict_values = dict()
	
	for set_element in set_values:
		counter = list_values.count(set_element)
		dict_values[set_element] = counter
	
	print(dict_values)
	
	return dict_values

#START HERE
# dict_count(["a", "a", "a", "b", "c", "d", "c", "b", "c", "d", "c", "e", "e", "e"])

#CALLING
# print(dict_count(["a", "a", "a", "b", "c", "d", "c", "b", "c", "d", "c", "e", "e", "e"]))