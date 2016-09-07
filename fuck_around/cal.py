import os

class Main_Program():
    def welcome_message(self):
        word = "Basic Calculator V0.1"
        print " "
        print "-" * len(word)
        print word
        print "-" * len(word)

    def dash_printing(self, word):
        print "-" * int(len(word) + 2)

    def options_menu(self):
        choice = raw_input("What would you like to do? \n1. Add \n2. Subtract \
                        \n3. Multiply \n4. Multiply \n5. Modulus \n>").lower()
        if choice == "1" or choice == "add":
            Calc_Options().addition()
        elif choice == "2":
            Calc_Options().subtraction()
        elif choice == "3":
            Calc_Options().testing()
        else:
            os.system('clear')
            print Main_Program().options_menu()

    def check_numtype(self, x):
        try:
            value = int(x)
            print "integer"
        except ValueError:
            value = float(x)
            print "float!"


class Calc_Options():

    """ def addition(self):
        print " "
        print "Addition"
        sentence = "Enter the first number: "
        Main_Program().dash_printing(sentence)
        x = float(raw_input("Enter the first number: "))
        y = float(raw_input("Enter the second number: "))
        print "%s + %s = %s" % (x, y, float(x + y))
        Main_Program().dash_printing("Enther the first number: ")
    """
# trying to create a progressional function
    def addition(self):
        print " "
        print "Addition"
        sentence = "Enter number: "
        Main_Program().dash_printing(sentence)
        num_list = []
        while len(num_list) < 10:
            x = raw_input(">")
            if x.isdigit():
                num_list.append(float(x))
            else:
                print "Not a valid number!"
            if x == "=":
                print "Total: {}".format(sum(num_list))
                break
            if len(num_list) == 10:
                print "Total: {}".format(sum(num_list))
                break

    def subtraction(self):
        print " "
        print "Subtraction"
        sentence = "Enther the first number: "
        Main_Program().dash_printing(sentence)
        x = int(raw_input("Enter the first number: "))
        y = int(raw_input("Enter the second number: "))
        print "%s - %s = %s" % (x, y, x - y)
        Main_Program().dash_printing("Enther the first number: ")

    def testing(self):
        print " "
        print "test"
        sentence = "Enther the first number: "
        Main_Program().dash_printing(sentence)
        x = raw_input("Enter the first number: ")
        Main_Program().check_numtype(x)
        y = raw_input("Enter the second number: ")
        Main_Program().check_numtype(y)
        print "%s + %s = %s" % (x, y, x + y)
        Main_Program().dash_printing("Enther the first number: ")


welcome = Main_Program()
welcome.welcome_message()
welcome.options_menu()
