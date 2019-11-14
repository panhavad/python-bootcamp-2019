from datetime import *

def date_time():
	"""Give date and time with this format YYYY-MM-DD HH:MM:SS

    Args:
      NONE
    Returns:
      date and time in string format of YYYY-MM-DD HH:MM:SS
    """
	current_datetime = datetime.now()
	str_current_datetimestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S") #YYY-MM-DD hh-mm-ss
	
	print(str_current_datetimestamp)
	
	return str_current_datetimestamp

#START HERE
# date_time()

#CALLING
# print(date_time())
# print(type(date_time()))