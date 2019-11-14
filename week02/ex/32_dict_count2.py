def dict_count2(list_values):
	"""Count and sort by value if same value sort by key

    Args:
      simple value
    Returns:
      
    """
	
	new_list_values = list()
	res_list = list()
	occurrence_set = set()
	total_occorrences = 0
	
	if list_values != []:
		set_values = sorted(set(list_values)) #short way to get the unique value in list
		
		for set_element in set_values:
			occurrence_counter = list_values.count(set_element)
			total_occorrences += occurrence_counter
			occurrence_set.add(occurrence_counter)
			new_list_values.append((set_element, occurrence_counter))#add tuple to list

		while len(res_list) != len(set_values):
			for each_list in new_list_values:
				if each_list[1] == max(occurrence_set):
					res_list.append(each_list)
			occurrence_set.remove(max(occurrence_set))

		print(f"{res_list}\n"
				f"TOTAL: {total_occorrences}")

		return res_list

	else:
		print(f"Your string is empty.\n"
				f"TOTAL: {total_occorrences}")
		
		return list_values
		

#START HERE
# dict_count2(["z", "z", "z", "z", "b", "b", "b", "b", "b", "a", "a", "a", "a", "a"])
# dict_count2([])

#CALLING
print(dict_count2(["z","z", "z", "z", "b", "b", "b", "b", "a", "a", "a", "a", "a", "a"]))
print(dict_count2([]))
