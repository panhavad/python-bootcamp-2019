"""
	
	NB: In this program we handle invalid character in param but
		we do not handle the epoch value as NEGATIVE because epoch value
		can be NEGATIVE

		proof by https://www.epochconverter.com/

"""
import time

def timestamp_to_str(str_timestamp):
	"""Converting epoch number to the actual date and time

    Args:
      string of epoch value
    Returns:
      actual date and time as string in format of YYYY-MM-DD HH:MM:SS
    """
	try:
		str_timestamp = int(str_timestamp)
		converted_datetime = time.strftime("%Y-%m-%d %H:%M:%S", 
			time.gmtime(str_timestamp+25200))
		
		print(converted_datetime)
		
		return converted_datetime
	except Exception as e:
		print("Your timestamp is not valid.")
		
		return 0

#START HERE
# timestamp_to_str(1545730073)
# timestamp_to_str("sad")
# timestamp_to_str(-1)


#CALLING
# print(timestamp_to_str(1623646780))
# print(timestamp_to_str("sad"))