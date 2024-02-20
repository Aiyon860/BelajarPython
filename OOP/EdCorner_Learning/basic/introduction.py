class Human:
    # like a constructor in Java
    """ 
        When we create instance or object out of class (blueprint/model),
        we must at first initialize the object by using __init__() function first.
    """
    # instance attribute/information (variables that defined inside a class function)  
    def __init__(self, name: str, age: int, gender: str, city: str, married: bool):
        self.name = name
        self.age= age
        self.gender= gender
        self.city = city
        self.married = married

    # class attribute, has fixed value for all instances or objects of class.
    species = "Homo Sapiens"

    # instance method
    def speak(self):
        return f"Hello everyone! I am {self.name}."
    
    # instance mthod
    def eat(self, favouriteDish):
        return f"I love to eat {favouriteDish}!!!"

# x and y are instances of class Human
x = Human("Daniel", 18, "Male", "Semarang", False)
y = Human("Tirza", 18, "Female", "Semarang", False)

""" 
    although it all derived from the same blueprint/class, the result is still false
    because when each object is created it reserved a memory space respectively/differently. 
"""
# print(x == y);
# this is the prove.
# print(x);
# print(y);

# species are class attribute, hence will have same value for all instances.
print(x.species)
print(y.species, "\n")

# setting new value for class attribute
Human.species = "Sapiens"
print(x.species)
print(y.species, "\n")

# name, age, gender, city, and married status will have different values per instance, because they are instance attributes.
print(x.name)
print(y.name)
print(f"\nHello, my name is {x.name}. I am {x.age} years old. I'm {x.gender}. I'm from {x.city} City. Married: {x.married}.")
print(f"Hello, my name is {y.name}. I am {y.age} years old. I'm {y.gender}. I'm from {y.city} City. Married: {y.married}.")

print("")

# testing instance method (speak)
print(x.speak())
print(y.speak())
# testing instance method (eat)
print(x.eat("Burger"))
print(x.eat("Pizza"))
