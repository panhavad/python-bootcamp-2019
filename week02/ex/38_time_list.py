from datetime import *
import time

def time_list(number_sec):
	"""Store time in this format HH:MM:SS to the list base
		on the second given

    Args:
      number of second program have to generate the current time
    Returns:
      list of time in each second
    """
	time_list_values = list()
	
	try:
		number_sec = int(number_sec)
		
		if number_sec > 0:
	
			for interval in range(0, number_sec):
				current_datetime = datetime.now() #this can also be done in one line
				current_time = current_datetime.strftime("%H:%M:%S") #but do this will make it more readable
				time_list_values.append(current_time)
				time.sleep(1)
			print(time_list_values)
			
			return time_list_values
		else:
			raise
	except Exception as e:
		print(f"{time_list_values}\n"
				"Invalid integer.")
		
		return time_list_values

#START HERE
# time_list(4)
# time_list(-4)
# time_list("2")
# time_list("asd&^")


#CALLING
# print(time_list(4))
# print(time_list(-4))
# print(time_list("2"))
# print(time_list("&^&*&SDJK"))

