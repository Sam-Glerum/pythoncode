#Program which converts Fahrenheit to Celsius

def f_to_c():
	x = float(raw_input("Enter Fahrenheit temp: "))
	y = (5.000 / 9.000) * (x - 32.000)
	print y

f_to_c()
