def top_words(single_str):
	"""Main function that use to give the result of top maximum 3 value

    Args:
      single string
    Returns:
      [] when the input is empty string
      [top 3,2,1] when input is valid with lowercase result     
    """

	unique_list = list()
	counter_dict = dict()
	final_list = list()
	index = 0

	MAX_TOP_WORDS = 3 #the maximum top word will display

	if len(single_str) > 0:
		
		original_list = clean_split(single_str)

		for list_element in original_list:
			if list_element[0].isalpha() == False:
				original_list[index] = list_element.replace(list_element[0], "")
			if list_element[-1].isalpha() == False:
				original_list[index] = list_element.replace(list_element[-1], "")
			index += 1

		unique_list = list_to_unique(original_list)
		counter_dict = occurences_into_dict(unique_list, original_list)

		while len(final_list) < MAX_TOP_WORDS:
			max_in_dict = max(counter_dict.values())
			if max_in_dict == 0:
				break
			
			for dict_element in counter_dict:
				if counter_dict[dict_element] == max_in_dict and counter_dict[dict_element] != 0:
					final_list.append(dict_element)
					counter_dict[dict_element] = 0
					break
	
	print(final_list)
	
	return final_list

def clean_split(original_string):
	"""Subset function that help to split the given string with space and
		clean out all the bad element like ""

    Args:
      the very first original string
    Returns:
      splited and clean string 
    """
	
	splited_list = original_string.lower().split(" ")
	clean_split_list = list()
	
	for list_element in splited_list:
		if len(list_element) > 0:
			clean_split_list.append(list_element)
	
	return clean_split_list


def list_to_unique(original_list):
	"""Subset function to going to return back the unique value in the list only

    Args:
      original string from the main function
    Returns:
      the list of unique value from the original list   
    """
	
	unique_list = list()
	
	for list_element in original_list:
		if list_element not in unique_list:
			unique_list.append(list_element)
	
	return unique_list

def occurences_into_dict(unique_list, original_list):
	"""Subset function to put all the element and its occurences time in the dictionary
		as key and value

    Args:
      list that already filter unique value
      original list from main function
    Returns:
      dictionary with pair of element name as key and its occurences time as value   
    """
	
	counter_dict = dict()
	
	for unique_list_element in unique_list:
		occurences_counter = original_list.count(unique_list_element)
		counter_dict[unique_list_element] = occurences_counter
	
	return counter_dict

#START HERE
# top_words("Welcome to Kirirom: Kirirom Institute of Technology" 
# 	" and Kirirom National Parc. To contact us, send a message to us!")

# top_words("can’t/ cant Cant can’t")

# top_words("hello hello Hello")

# top_words(". ??? // ####### // // ???")

# top_words("hi hello hi wow wow hello good good good   ")

#CALLING
# print(top_words("Welcome to Kirirom: Kirirom Institute of Technology"
# 	" and Kirirom National Parc. To contact us, send a message to us!"))

# print(top_words("can’t/ cant Cant can’t"))

# print(top_words("hello hello Hello"))

# print(top_words(". ??? // ####### // // ???"))

# print(top_words("hi hello hi wow wow hello good good good   "))


