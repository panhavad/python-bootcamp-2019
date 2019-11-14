"""
	INTRUCTION: Base on the requirement as of now no
				need to handle the string with space
				just take the first character for acronym

	WARNING: No need to handle the [] empty list condition because if 
			empty list will be nothing to loop and store so use same code
			no condition required

"""
def acronym(list_values):
	"""Take the first character of each element in list
		store in new list

    Args:
      a list of anything
    Returns:
      list of single uppercase letter
    """
	list_acronym = list()
	
	for list_element in list_values:
			
			try:
				
				if len(list_element) > 0:
					list_acronym.append(list_element[0].upper())
				else:
					list_acronym.append("")#handle when string is empty 
			
			except Exception as e:
				#this will handle if the input is number
				#not importance but you might use this to crash my program :)
				to_str = str(list_element)
				list_acronym.append(to_str[0])
	
	print(list_acronym)
	
	return list_acronym

#START HERE
# acronym([89, "wide", "web"])
# acronym([])
# acronym(["", "wide", "web"])

#CALLING
# print(acronym([89, "wide", "web"]))
# print(acronym([]))
# print(acronym(["", "wide", "web"]))

