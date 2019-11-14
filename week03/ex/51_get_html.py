import requests

def get_html(url):
	'''Get the html code of website as string
		Arg: website url
		Return: html code in form of string from URL
	'''
	req_obj = requests.get(url)
	return req_obj.text

print(get_html("https://httpbin.org/"))