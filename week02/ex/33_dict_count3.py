def dict_count3(list_values):
	"""Sort the list of tuple that created by
		the given list

    Args:
      a list of anything
    Returns:
      list of sorted tuple
      total repeat time of all elemet in list of tuple
    """

	total_occorrences = 0
	
	if list_values != []:
		set_values = set(list_values)
		sorted_list_values = list()
		
		for set_element in set_values:
			occorrence_counter = list_values.count(set_element)
			sorted_list_values.append((set_element, occorrence_counter))
			total_occorrences += occorrence_counter
		
		sorted_list_values = sorted(sorted_list_values)
		print(f"{sorted_list_values}\n"
				f"TOTAL: {total_occorrences}")
		
		return sorted_list_values
	
	else:
		print(f"Your string is empty.\n"
				f"TOTAL: {total_occorrences}")
		
		return list_values

#START HERE
dict_count3(["a", "b", "b", "c", "c", "c", "c", "d", "d", "e", "e", "e"])
# dict_count3([])

#CALLING
# print(dict_count3(["a", "b", "b", "c", "c", "c", "c", "d", "d", "e", "e", "e"]))
# print(dict_count3([]))

