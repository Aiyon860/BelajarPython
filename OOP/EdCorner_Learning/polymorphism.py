# learning polymorphism
""" 
    Something can be in various forms, or
    depending on the circumstance, can exhibit a variety of behaviours.

    Function with the same name can have different behaviors.
"""

# in-built polymorphism function
print(len("This is String."))
print(len([1, 2, 3, 4, 5]))
print(len({
    '1':"AWS",
    '2':"Amazon",
    '3':"Kindle"
}))

print()

# polymorphism with '+' operator
x = 5 + 5
y = 'python' + 'programming'
z = 3.5 + 3
print(x)    # addition operation with both ints
print(y)    # concatenate string 
print(z)    # addition operation with float and int

print()

# Class Methods and Polymorphism
class Lion:
    # constructor
    def __init__(self) -> None:
        pass

    # class methods (i think because it doesn't contain the instance properties inside the function(?))
    def color(self) -> None:
        print("The Lion is yellow coloured.")
    def eats(self) -> None:
        print("The Lion eats a lot!")

class Deer:
    # constructor
    def __init__(self) -> None:
        pass

    # class methods
    def color(self) -> None:
        print("The Deer is white coloured.")
    def eats(self) -> None:
        print("The Deer eats less!")

lion = Lion()
deer = Deer()

for animal in (lion, deer):
    animal.color()
    animal.eats()

""" ---------------------------------------------------- """
print()
""" ---------------------------------------------------- """

# Inheritance and Polymorphism
class Shape:
    def __init__(self) -> None:
        pass

    def no_of_slides(self) -> None:
        pass
    def three_dimensional(self) -> None:
        print("I am 3D from Shape class.")

class Rectangle(Shape):
    def no_of_slides(self) -> None:
        print("I have 4 sides. I am from Rectangle class.")

class Triangle(Shape):
    def no_of_slides(self) -> None:
        print("I have 3 sides. I am from Triangle class.")

# Making object from Rectangle class
rectangle = Rectangle()
# Override the no_of_slides of parent class
rectangle.no_of_slides()

# Making object from Triangle class
triangle = Triangle()
# Override the no_of_slides of parent class
triangle.no_of_slides()