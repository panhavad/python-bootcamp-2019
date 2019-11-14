from datetime import *

def current_date():
	"""Print the current date in this format YYYY-MM-DD

    Args:
      no parameter needed
    Returns:
      the current date type of string in this format YYYY-MM-DD
    """
	current_datetime = datetime.now()
	str_current_date = current_datetime.strftime("%Y-%m-%d") #YYYY-MM-DD
	
	print(str_current_date)
	
	return str_current_date


#START HERE
# current_date()

#CALLING
# print(current_date())
# print(type(current_date())) #type check