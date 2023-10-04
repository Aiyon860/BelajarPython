from assets.helper import *

# The self parameter refers to the instance of the object (like 'this' is Java and C++).

# __init__ function is obligatory when we making the object of the class.
class Pet:
    def __init__(self, intro, favPet):
        self.intro = intro
        self.favPet = favPet

mypet = Pet("Hello Guys, My Name is Daniel", "Cat")
print(mypet.intro)
print(mypet.favPet)

FreeSpace()

# __str__ function
class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Username: {self.username}\nPassword: {self.password}"

request = Login("Aiyon", "123456")
print(request)
# instead of <__main__.Login object at 0x0000022D3DE72490>
# when we use str func, at the end we got this instead (line 24)

FreeSpace()

# Object Methods
class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def buy(self):
        print("Product Name: " + self.name + "\nProduct Price: " + f"{self.price}")
    
consumer = Product("Chocolate", 20_000)
consumer.buy()

FreeSpace()

""" 
'self' parameter, reference to the current instance of the class, 
and is used to access variables that belongs to the class.

It does not have to be named self , 
you can call it whatever you like, 
but it has to be the first parameter of any function in the class
"""
class Teacher():
    def __init__(random, name, subject):
        random.name = name
        random.subject = subject
        random.weather = []

    def greetings(random, checkWeather):
        if "Morning" in checkWeather:
            random.weather.append("Morning")
        elif "Afternoon" in checkWeather:
            random.weather.append("Afternoon")
        elif "Evening" in checkWeather:
            random.weather.append("Evening")
        else:
            random.weather.append('0')

        i = 0
        if random.weather[i] == '0':
            print("Wrong Input!")
        else:
            print("Good " + random.weather[i] + " My Students!\nMy Name is " + 
                  random.name + " and I will Teach You " + random.subject +  " Lesson")

FirstTeacher = Teacher("Bambang", "OOP")
FirstTeacher.greetings("Morning")

FreeSpace()

# Modify Object Properties
class Pair():
    def __init__(self, man, woman):
        self.husband = man
        self.wife = woman
        self.child = 0
    
    def manyChild(self):
        if self.child == 0:
            print(self.husband + " and " + self.wife + " have " + f"{self.child}" + " child")
        else:
            print(self.husband + " and " + self.wife + " have " + f"{self.child}" + " children")

FirstPair = Pair("Daniel Adi Pratama", "Tirza Nadya Wibowo")
FirstPair.manyChild()
FirstPair.child = 3
FirstPair.manyChild()

FreeSpace()

# Delete Object Properties ('del')
class PairTwo():
    def __init__(self, man, woman):
        self.husband = man
        self.wife = woman
        self.child = 0

FirstPair = PairTwo("Daniel Adi Pratama", "Tirza Nadya Wibowo")
print("Total Child: " + f"{FirstPair.child}")
del FirstPair.child
# print(FirstPair.child) got deleted because of a 'del' keyword

FreeSpace()

# Delete Objects
class PairThree():
    def __init__(self, man, woman):
        self.husband = man
        self.wife = woman
        self.child = 0

    def __str__(self):
        return f"{self.husband} + {self.wife}"

FirstPair = PairThree("Daniel Adi Pratama", "Tirza Nadya Wibowo")
print(FirstPair)
del FirstPair
# print(FirstPair) got deleted because of a 'del' keyword

FreeSpace()

# pass statement
""" class definitions cannot be empty, but if you for some reason have a class definition with no content, 
put in the pass statement to avoid getting an error. """
class Test:
    pass

FreeSpace()