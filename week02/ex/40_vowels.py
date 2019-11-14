def vowels(single_str):
	"""display vowels count and display non-vowel not space

    Args:
      any single string
    Returns:
      0
      number of vowels
      non-vowels as string
    """
	vowels_list = ["a", "e", "i", "o", "u"]
	vowels_collecter = ""
	others_collecter = ""
	single_str = str(single_str).replace(" ", "")

	for character in single_str:
		
		if character in vowels_list:
			vowels_collecter += character
		else:
			others_collecter += character

	if len(vowels_collecter) == 0:
		print("NO VOWELS")
		
		return 0
	else:
		print(f"{len(vowels_collecter)}\n"
				f"{vowels_collecter}\n"
				f"{others_collecter.upper()}")
		
		return len(vowels_collecter)

#START HERE
# vowels("what is that ?")
# vowels("aeiou")
# vowels(123)



#CALLING
# print(vowels("what is that ?"))
# print(vowels("aeiou"))
# print(vowels(123))
