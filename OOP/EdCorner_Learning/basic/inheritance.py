# learning inheritance

# body of parent class.
class Human:
    # constructor
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name;
        self.age = age;
        self.gender = gender;

    # instance method
    def description(self) -> None:
        print(f"Hey! My name is {self.name}, I'm a {self.gender} and I'm {self.age} years old.")
    def code(self) -> None:
        print("I can code.")

# inherits the parent class, body of child class.
class Boy(Human):
    def schoolName(self, schoolName) -> None:
        print(f"I {self.name} study in {schoolName}.")

class Girl(Human):
    def schoolName(self, schoolName) -> None:
        print(f"I {self.name} study in {schoolName}.")
    def code(self) -> None:
        print("I can teach.")
    def activity(self) -> None:
        super().code() # taking the "code" method from parent.

# object from Boy class (child)
b = Boy("Daniel", 19, "Male")
b.description()
b.schoolName("Politeknik Negeri Semarang")

print()

# cannot call schoolName method if its not from child class (Boy) object
a = Human("Tirza", 19, "Female")
a.description()
# a.schoolName("Universitas Diponegoro") --> AttributeError: 'Human' object has no attribute 'schoolName'

print()

# testing super() method
g = Girl("Lisa", 17, "Female")
g.description()
g.activity()