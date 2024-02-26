""" 
    Module 1 Class Method - Decorator
"""

# ------------------------------------------------------------- #

class Person:
    def show_details(cls):
        print(f"Running from {cls.__name__} class.")
    
    # convert function to class method
    show_details = classmethod(show_details)

Person.show_details()

print() # ------------------------------------------------------------- #

class Container:
    @classmethod
    def show_details(cls):
        print(f"Running from {cls.__name__} class.")

Container.show_details()
container = Container()
container.show_details()

print() # ------------------------------------------------------------- #

class PersonTwo:
    instances = []

    def __init__(self) -> None:
        PersonTwo.instances.append(self)

    @classmethod
    def count_instances(cls) -> int:
        return len(PersonTwo.instances)

p1 = PersonTwo()
p2 = PersonTwo()
p3 = PersonTwo()

print(f"Amount of PersonTwo's instances created are {PersonTwo.count_instances()}")

print() # ------------------------------------------------------------- #

class PersonThree:
    instances = []

    def __init__(self, firstName: str, lastName: str) -> None:
        self.firstName = firstName
        self.lastName = lastName
        PersonThree.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(PersonThree.instances)
    
pp1 = PersonThree("Daniel", "Adi Pratama")
pp2 = PersonThree("Tirza", "Nadya Wibowo")

print(f"Amount of PersonThree's instances created are {PersonThree.count_instances()}.")

