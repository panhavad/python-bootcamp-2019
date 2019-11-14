def list_sort_str(list_values):
	"""Keep only string on the list and sorted

    Args:
      a single list of anything
    Returns:
      a sorted list of string not digit
    """
	set_values = set()

	for list_element in list_values:
		try:
			int(list_element)
		except Exception as e:
			set_values.add(list_element)

	list_values.clear()

	for set_element in set_values:
		list_values.append(set_element)
		
	sorted_list_values = sorted(list_values)
	print(sorted_list_values)

	return sorted_list_values

#START HERE
# list_sort_str(["abc", "4", "2", "3", "dza", "def"])

#CALLING
# print(list_sort_str(["abc", "4", "2", "3", "dza", "dza", "def"]))