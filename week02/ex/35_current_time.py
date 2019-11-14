from datetime import *

def current_time():
	"""Give the current time with this format HH:MM:SS

    Args:
      NONE
    Returns:
      a current time in string format of HH:MM:SS
    """
	current_datetime = datetime.now()
	str_current_timestamp = current_datetime.strftime("%H:%M:%S")#hh:mm:ss
	
	print(str_current_timestamp)
	
	return str_current_timestamp

#START HERE
# current_time()

#CALLING
# print(current_time())
# print(type(current_time())) #type checker