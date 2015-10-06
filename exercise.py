'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class Exercise():
	
	def __init__(self):
		self.user_input = ""
	
	def getString(self):
		self.user_input = raw_input("Enter a string: ")
		
	def printString(self):
		print self.user_input.upper()
		
def test():
	test_var = Exercise()
	test_var.getString()
	test_var.printString()
	
	
test()

