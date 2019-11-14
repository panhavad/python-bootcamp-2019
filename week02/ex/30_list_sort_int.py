def list_sort_int(list_values):
	"""Remove all not digit and sorted the existence

    Args:
      a list of anything
    Returns:
      a list of digit that have been sorted
    """
	set_values = set()

	for list_element in list_values:
		try:
			converted_list_value = int(list_element)
			set_values.add(converted_list_value)
		except Exception as e:
			continue
	
	list_values.clear()
	
	for set_element in set_values:
		list_values.append(set_element)
	
	sorted_list_values = sorted(list_values)
	print(sorted_list_values)

	return sorted_list_values

#START HERE
# list_sort_int(["abc", "4", "2", "2", "3", "dza", "dza", "def"])

#CALLING
# print(list_sort_int(["abc", "4", "2", "3", "dza", "dza", "def"]))