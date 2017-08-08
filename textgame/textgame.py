class Human():

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is {0}").format(self.name)

sam = Human("Sam")
sam.greet()
