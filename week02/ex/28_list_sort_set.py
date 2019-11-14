def list_sort_set(list_values):
	"""Sorted the given list but keep only unique value

    Args:
      single list of anything
    Returns:
      sorted unique list vlaue
    
    This is not good performance
	set_values = set()
	for list_element in list_values:
		set_values.add(list_element)
	list_values.clear()
	for set_element in set_values:
		list_values.append(set_element)
	sorted_list_value = sorted(list_values)
	print(sorted_list_value)

	"""

	list_values = set(list_values)
	list_values = list(sorted(list_values))

	print(list_values)

	return list_values

#START HERE
# list_sort_set([4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5])

#CALLING
# print(list_sort_set([4, 2, 19, 50, 49, 48, 1, 2, 3, 4, 5]))