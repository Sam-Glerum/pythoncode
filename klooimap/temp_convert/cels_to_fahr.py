#Program which converts Celsius to Fahrenheit

def c_to_f():
	x = float(raw_input("Enter Celsius temp: "))
	y = (9.000 / 5.000) * x + 32.000
	print y

c_to_f()
