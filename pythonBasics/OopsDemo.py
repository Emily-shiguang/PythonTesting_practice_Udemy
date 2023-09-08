# Two types of variables which have whole different purpose: class variable, instance variable
# self keyword is mandatory for calling variable names into method
# constructor name should be __init__
# new keyword is not required when you create object

class Caculator:
    num = 100  # class variables
    # default constructor

    def __init__(self, a, b):
        self.firstNumber = a  # firstNumber and secondNumber are instance variables
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):  # define method inside the class
        print("I am now execution as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Caculator.num

obj = Caculator(2, 3)  # syntax to create objects in Python
obj.getData()
print(obj.Summation())

obj1 = Caculator(4, 5)  # syntax to create objects in Python
obj1.getData()
print(obj1.Summation())


