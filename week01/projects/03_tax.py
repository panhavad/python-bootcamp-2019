"""
	
	STEPS:	
		- Instruction message
		- Get input as number
		- Give next instruction
		- Get input as number
		- Display warning if exited 1 to 99 value
		- Display calculation result in this form

	WARNING:
		- No negative numbers
		- Tax rate only from 1 to 99
	
	FORBIDEN:
		- No misspelling
	
	RECOMMENDED:
		- Using CONSTANT
		- String format
		- {:.2f}'.format(amount)
	
	TESTED:
		- Amount input    OK
			- Alphabet    OK
			- Negative numbers    OK
			- Float    OK
			- Special symbol    OK
			- Blank    OK
		- Rate input    OK
			- Alphabet    OK
			- Negative numbers    OK
			- Float    OK
			- Special symbol    OK
			- Blank    OK

"""

AMOUNT_MESSAGE = "Please enter your amount:\n"
RATE_MESSAGE = "Please enter tax rate:\n"

NUMBER_WARNING = "Number is incorrect, try again."
RATE_WARNING = "Rate is incorrect, try again."


def input_amount():
	try:
		amount = float(input(AMOUNT_MESSAGE))
		if amount > 0:
			return amount
		else:
			#raise exception when come here
			#best practice not to repeat same code
			raise
	except Exception as e:
		print(NUMBER_WARNING)
		return input_amount()
	

def input_rate():
	try:
		rate = float(input(RATE_MESSAGE))
		if rate >= 1 or rate <= 99:#can not use range here because we want range of float
			return rate
		else:
			raise
	except Exception as e:
		print(RATE_WARNING)
		return input_rate()


def tax_calculation(amount, rate):
	return amount * rate / 100


def net_calculation(amount, rate):
	return amount - tax_calculation(amount, rate)


#START HERE
amount = input_amount()
rate = input_rate()

#final output
print("===== ===== ===== ===== =====\n"
	f"AMOUNT: {amount}$\n"
	f"RATE: {rate}%\n"
	"===== ===== ===== ===== =====\n"
	f"TAX: {'{:.2f}'.format(tax_calculation(amount, rate))}$\n"
	f"NET: {'{:.2f}'.format(net_calculation(amount, rate))}$\n"
	"===== ===== ===== ===== =====\n")