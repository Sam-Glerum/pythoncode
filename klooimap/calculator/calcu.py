#Calculator, to refresh Python
import os
#os.system('cls' if os.name == 'nt' else 'clear')



class Program():
	
	def draw_dash(self, x, word):
		print "-" * (len(x) + 1)
		print word
		print "-" * (len(x) + 1)

	def welcome_user(self):
		welcome_message = "Welcome to CalPy, the Python-made calculator"
		Program().draw_dash(welcome_message, welcome_message)

	def user_choice(self):
		print "\nWhat would you like to do? (Enter the number and press Enter)"
		choice = raw_input("1. Add (+) \n2. Subtract (-) \n3. Divide (/) \n4. Multiply (*) \n5. Modulo (%) \n\nChoice: ")
		
		if choice == '1':
			os.system('cls' if os.name == 'nt' else 'clear')
			Calculations().add()
		elif choice == '2':
			os.system('cls' if os.name == 'nt' else 'clear')
			Calculations().subtract()


			'''Trying to replace the last part of the add() function in Calculations()'''
	def go_again(self, operation):
		self.operation = operation
		print "\n1. Main Menu \n2. Again"
		question = raw_input("What would you like to do? ")
		if question == '1':
			os.system('cls' if os.name == 'nt' else 'clear')
			message.welcome_user()
			message.user_choice()
		elif question == '2':
			os.system('cls' if os.name == 'nt' else 'clear')
			return operation
		else:
			go_again(operation)




class Calculations(Program):
	#class for calc methods
	def add(self):
		#print addition_welcome_message
		start_adding = "Start adding"
		Program().draw_dash(start_adding, start_adding)
		
		#print prompt, wait for user_input
		x = raw_input("Enter first number: ")
		y = raw_input("Enter second number: ")
		z = (x + y)

		#print result of calculation, + dashes
		result_text = "Result: %s" % z
		Program().draw_dash(result_text, result_text)
		Program().go_again(Calculations().add())

		'''
		print "\n1. Main Menu \n2. Again"
		question = raw_input("What would you like to do? ")
		if question == '1':
			os.system('cls' if os.name == 'nt' else 'clear')
			message.welcome_user()
			message.user_choice()
		elif question == '2':
			os.system('cls' if os.name == 'nt' else 'clear')
			Calculations().add()
		elif question != '1' or '2':
			os.system('cls' if os.name == 'nt' else 'clear')
			print question
		'''

	def subtract(self):
		print "Start subtracting"

message = Program()

message.welcome_user()
message.user_choice()