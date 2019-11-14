import requests

def get_fbid(fb_url_id):
	''' Getting the facebook ID from the website findmyfbid.com
		Arg: name or facebook url
		Return: tuple of (status code, id)
	'''
	data = {'url' : fb_url_id}
	try:
		req_obj = requests.post("https://findmyfbid.com", data = data)
		res_fb_id = req_obj.json()['id']
	except requests.exceptions.ConnectionError as e:#when no internet connection
		print("Please connection to the internet!")
		exit()
	except TypeError as e:#when [id] is not exist
		res_fb_id = 0
		
	return (req_obj.status_code, res_fb_id)

# print(get_fbid("zucklllll"))
# print(get_fbid("panhavad"))
# print(get_fbid("hts://facebook.com/panhavassssd"))
