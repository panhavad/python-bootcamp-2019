import requests, time


def get_currency(pairs_list):
	''' Get the currency, rate, timestamp, datetime of the given currency
		Arg: List of currency pair that available in forex
		Return: List of tuple detail about those pair currency
	'''
	endpoint_url = "https://www.freeforexapi.com/api/live"
	res_list = list()
	
	for currency in pairs_list:
		pairs_dict = {'pairs' : currency}
		try:
			api_req = requests.post(url = endpoint_url, params = pairs_dict)
		
			if api_req.status_code == 200:
				api_respond = api_req.json()
				
				if api_respond['code'] == 200:
					rates_dict = api_respond['rates'][currency]
					rate, timestamp_int = rates_dict['rate'], int(rates_dict['timestamp'])
					datetime_str = time.strftime("%d/%m/%Y %H:%M", time.localtime(timestamp_int))
					res_tuple = (currency, rate, timestamp_int, datetime_str)
					res_list.append(res_tuple)
				
				else:
					print(f"The currency pair {currency} was not recognised or supported")
		except requests.exceptions.ConnectionError as e:
			print("Please connection to the internet!")
			return res_list
			exit()

	return res_list


# print(get_currency(["AUdDUSD"]))
print(get_currency(["AUDUSD","EURGBP","EURUSD","GBPUSD","JUSTKIDDING"]))
# print(get_currency([]))
