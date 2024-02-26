""" 
    Module 3 Special Methods

    The __str__() method returns a human-readable, or informal, string representation of an object.
    If you dont define a __str__() method for a class, then the built-in object implementation calls the __repr__() method instead.

    The __repr__() method returns a more information-rich, or official, string representation of an object.
    In all cases, the string should be informative and unambiguous.

    In general, the __str__() string is intended for users and the __repr__() string is intended for developers.

    Note that str() and repr() return the same value, because str() calls __repr__() when __str__() isn’t implemented.
"""

# import
import uuid

print("Start")

print() # --------------------------------------------------------------------- #

class Person:
    # constructor
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname
    
    # return the formal representation of the Person object
    def __repr__(self) -> str:
        return f"Person(fname = '{self.fname}', lname = '{self.lname}')."
    
person = Person("Mike", "Smith")
print(person)

print() # ------------------------------------------------------------- #

class PersonTwo:
    # constructor
    def __init__(self, fname: str = None, lname: str = None) -> None:
        self.fname = fname
        self.lname = lname

    # return the formal representation of the PersonTwo object
    def __repr__(self) -> str:
        return f"PersonTwo(fname = '{self.fname}', lname = '{self.lname}')."

    # return the informal representation of the PersonTwo object
    def __str__(self) -> str:
        return f"fname = '{self.fname}'\nlname = '{self.lname}'."
    
personTwo = PersonTwo("Mike", "Smith")
print(personTwo)
personThree = PersonTwo()
print(personThree)

print() # ------------------------------------------------------------- #

class Vector:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components
    
    # return the formal representation of Vector 
    def __repr__(self) -> str:
        return f"Vector{self.components}"
    
vl = Vector(1, 2)
print(vl)
v2 = Vector(-3, 4, 2)
print(v2)

print() # ------------------------------------------------------------- #

class VectorTwo:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
        
v3 = VectorTwo(1, 2)
print(v3)
v4 = VectorTwo(-3, 4, 2)
print(v4)

print() # ------------------------------------------------------------- #

class VectorThree:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
    
    # return the number of Vector coordinates (this is a must if you want to use len function over this object)
    def __len__(self) -> int:
        return len(self.components)

""" 
    If you haven't define the __len__() method before in the class,
    then when you use len function to know the length of the instance it will throw an error

    TypeError: object of type 'VectorThree' has no len()
"""
v5 = VectorThree(5, 6, 7)
print(len(v5))
v6 = VectorThree()
print(len(v6))

print() # ------------------------------------------------------------- #

class VectorFour:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
    
    # return the number of Vector coordinates
    def __len__(self) -> int:
        return len(self.components)
    
    # return the logical value of the Vector
    def __bool__(self) -> bool:
        if not self.components:
            return False
        return False if not self.components[0] else True

v7 = VectorFour()
v8 = VectorFour(3, 2)
v9 = VectorFour(0, -3, 2)
v10 = VectorFour(5, 0, -1)

print(bool(v7))
print(bool(v8))
print(bool(v9))
print(bool(v10))

v11 = VectorFour(4, 2)
v12 = VectorFour(-1, 3)
try:
    v11 + v12
except TypeError as error:
    print(error)

print() # ------------------------------------------------------------- #

class VectorFive:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
    
    # return the number of Vector coordinates
    def __len__(self) -> int:
        return len(self.components)
    
    # return the logical value of the Vector
    def __bool__(self) -> bool:
        if not self.components:
            return False
        return False if not self.components[0] else True

    # __add__ is a special method that allows instances of a class to use the + operator for addition.
    def __add__(self, other) -> str:
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return VectorFive(*components)
    
v13 = VectorFive(4, 2)
v14 = VectorFive(-1, 3)
print(v13 + v14)

print() # ------------------------------------------------------------- #

class VectorSix:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
    
    # return the number of Vector coordinates
    def __len__(self) -> int:
        return len(self.components)
    
    # return the logical value of the Vector
    def __bool__(self) -> bool:
        if not self.components:
            return False
        return False if not self.components[0] else True

    # __add__ is a special method that allows instances of a class to use the + operator for addition.
    def __add__(self, other) -> str:
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return VectorSix(*components)
    
    # __sub__ is a special method that allows instances of a class to use the - operator for substraction.
    def __sub__(self, other) -> str:
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return VectorSix(*components)

v15 = VectorSix(4, 2)
v16 = VectorSix(-1, 3)
print(v15 - v16)

print() # ------------------------------------------------------------- #

class VectorSeven:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
    
    # return the number of Vector coordinates
    def __len__(self) -> int:
        return len(self.components)
    
    # return the logical value of the Vector
    def __bool__(self) -> bool:
        if not self.components:
            return False
        return False if not self.components[0] else True

    # __add__ is a special method that allows instances of a class to use the + operator for addition.
    def __add__(self, other) -> str:
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return VectorSeven(*components)
    
    # __sub__ is a special method that allows instances of a class to use the - operator for substraction.
    def __sub__(self, other) -> str:
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return VectorSeven(*components)
    
    # __mul__ is a special method that allows instances of a class to use the * operator for multiplication.
    def __mul__(self, other) -> str:
        components = tuple(x * y for x, y in zip(self.components, other.components))
        return VectorSeven(*components)
    
v17 = VectorSeven(4, 2)
v18 = VectorSeven(-1, 3)
print(v17 * v18)

print() # ------------------------------------------------------------- #

class VectorEight:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
    
    # return the number of Vector coordinates
    def __len__(self) -> int:
        return len(self.components)
    
    # return the logical value of the Vector
    def __bool__(self) -> bool:
        if not self.components:
            return False
        return False if not self.components[0] else True

    # __add__ is a special method that allows instances of a class to use the + operator for addition.
    def __add__(self, other) -> str:
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return VectorEight(*components)
    
    # __sub__ is a special method that allows instances of a class to use the - operator for substraction.
    def __sub__(self, other) -> str:
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return VectorEight(*components)
    
    # __mul__ is a special method that allows instances of a class to use the * operator for multiplication.
    def __mul__(self, other) -> str:
        components = tuple(x * y for x, y in zip(self.components, other.components))
        return VectorEight(*components)
    
    # __truediv__ is a special method that allows instances of a class to use the / operator for division.
    def __truediv__(self, other) -> str:
        components = tuple(x / y for x, y in zip(self.components, other.components))
        return VectorEight(*components)

v19 = VectorEight(4, 2)
v20 = VectorEight(-1, 4)
print(v19 / v20)

print() # ------------------------------------------------------------- #

class VectorNine:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
    
    # return the number of Vector coordinates
    def __len__(self) -> int:
        return len(self.components)
    
    # return the logical value of the Vector
    def __bool__(self) -> bool:
        if not self.components:
            return False
        return False if not self.components[0] else True

    # __add__ is a special method that allows instances of a class to use the + operator for addition.
    def __add__(self, other) -> str:
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
    # __sub__ is a special method that allows instances of a class to use the - operator for substraction.
    def __sub__(self, other) -> str:
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
    # __mul__ is a special method that allows instances of a class to use the * operator for multiplication.
    def __mul__(self, other) -> str:
        components = tuple(x * y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
    # __truediv__ is a special method that allows instances of a class to use the / operator for division.
    def __truediv__(self, other) -> str:
        components = tuple(x / y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
    # __floordiv__ is a special method that allows instances of a classs to do integer division
    def __floordiv__(self, other) -> str:
        components = tuple(x // y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
v21 = VectorNine(4, 2)
v22 = VectorNine(-1, 4)
print(v21 // v22)

print() # ------------------------------------------------------------- #

class VectorTen:
    # constructor
    def __init__(self, *components) -> None:
        self.components = components

    # return the formal representation of VectorTwo
    def __repr__(self) -> str:
        return f"Vector{self.components}"

    # return the informal representation of VectorTwo
    def __str__(self) -> str:
        return f"{self.components}"
    
    # return the number of Vector coordinates
    def __len__(self) -> int:
        return len(self.components)
    
    # return the logical value of the Vector
    def __bool__(self) -> bool:
        if not self.components:
            return False
        return False if not self.components[0] else True

    # __add__ is a special method that allows instances of a class to use the + operator for addition.
    def __add__(self, other) -> str:
        components = tuple(x + y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
    # __sub__ is a special method that allows instances of a class to use the - operator for substraction.
    def __sub__(self, other) -> str:
        components = tuple(x - y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
    # __mul__ is a special method that allows instances of a class to use the * operator for multiplication.
    def __mul__(self, other) -> str:
        components = tuple(x * y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
    # __truediv__ is a special method that allows instances of a class to use the / operator for division.
    def __truediv__(self, other) -> str:
        components = tuple(x / y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
    # __floordiv__ is a special method that allows instances of a classs to do integer division
    def __floordiv__(self, other) -> str:
        components = tuple(x // y for x, y in zip(self.components, other.components))
        return VectorNine(*components)
    
# --------------------------------------------------------------------- #
print() # ------------------------------------------------------------- #
# --------------------------------------------------------------------- #

class Doc:
    # constructor
    def __init__(self, string: str) -> None:
        self.string = string
    
    # return formal representation of the object
    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"
    
    # return informal representation of the object
    def __str__(self) -> str:
        return f"{self.string}"
    
    # __add__ here is to concatenate two words into one sentence
    def __add__(self, other) -> str:
        return Doc(self.string + ' ' + other.string)

doc1 = Doc("Python")
doc2 = Doc("3.8")
print(doc1 + doc2)

print() # ------------------------------------------------------------- #

class Hashtag:
    # constructor
    def __init__(self, string: str) -> None:
        self.string = '#' + string
    
    # return formal representation of the object
    def __repr__(self) -> str:
        return f"Hashtag(string='{self.string}')"
    
    # return informal representation of the object
    def __str__(self) -> str:
        return f"{self.string}"
    
    # __add__ here is to concatenate two words into one sentence
    def __add__(self, other) -> str:
        return Hashtag(self.string[1:] + ' ' + other.string)

hashtag1 = Hashtag("python")
hashtag2 = Hashtag("developer")
hashtag3 = Hashtag("oop")

print(hashtag1 + hashtag2 + hashtag3)

print() # ------------------------------------------------------------- #

class DocTwo:
    # constructor
    def __init__(self, string: str) -> None:
        self.string = string
    
    # return formal representation of the object
    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"
    
    # return informal representation of the object
    def __str__(self) -> str:
        return f"{self.string}"
    
    # __add__ here is to concatenate two words into one sentence
    def __add__(self, other) -> str:
        return DocTwo(self.string + ' ' + other.string)
    
    # __eq__ is to check if the class instances are equal
    # i.e. have identical string attribute values
    def __eq__(self, other) -> bool:
        return self.string == other.string
    
doc3 = DocTwo("Python")
doc4 = DocTwo("3.8")
doc5 = DocTwo("Finance")
doc6 = DocTwo("Finance")

print(doc3 == doc4)
print(doc5 == doc6)

print() # ------------------------------------------------------------- #

class DocThree:
    # constructor
    def __init__(self, string: str) -> None:
        self.string = string
    
    # return formal representation of the object
    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"
    
    # return informal representation of the object
    def __str__(self) -> str:
        return f"{self.string}"
    
    # __add__ here is to concatenate two words into one sentence
    def __add__(self, other) -> str:
        return DocThree(self.string + ' ' + other.string)
    
    # __eq__ is to check if the class instances are equal
    # i.e. have identical string attribute values
    def __eq__(self, other) -> bool:
        return self.string == other.string
    
    # __it__ is to compare the class instances,
    # ex: when a class instance is smaller than another class instance when the string attribute is shorter
    def __lt__(self, other) -> bool:
        return len(self.string) < len(other.string)
    
doc7 = DocThree("Finance")
doc8 = DocThree("Education")
doc9 = DocThree("Apa itu Makanan?")
doc10 = DocThree("Hah?")
doc11 = DocThree("abc")
doc12 = DocThree("abc")

print(doc7 < doc8)
print(doc9 < doc10)
print(doc11 < doc12)

print() # ------------------------------------------------------------- #

class DocFour:
    # constructor
    def __init__(self, string: str) -> None:
        self.string = string
    
    # return formal representation of the object
    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"
    
    # return informal representation of the object
    def __str__(self) -> str:
        return f"{self.string}"
    
    # __add__ here is to concatenate two words into one sentence
    def __add__(self, other) -> str:
        return DocFour(self.string + ' ' + other.string)
    
    # __eq__ is to check if the class instances are equal
    # i.e. have identical string attribute values
    def __eq__(self, other) -> bool:
        return self.string == other.string
    
    # __it__ is to compare the class instances,
    # ex: when a class instance is smaller than another class instance when the string attribute is shorter
    def __lt__(self, other) -> bool:
        return len(self.string) < len(other.string)
    
    # __iadd__ is to perform extended assignments
    # ex: concatenate two instances with the string '&'
    def __iadd__(self, other) -> str:
        return DocFour(self.string + " & " + other.string)
    
doc13 = DocFour("Finance")
doc14 = DocFour("Accounting")
doc13 += doc14
print(doc13)

print() # ------------------------------------------------------------- #

class Book:
    # constructor
    def __init__(self, title: str = None, author: str = None) -> None:
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    # return informal representation of the object
    def __str__(self) -> str:
        return f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author}"

    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]
    
book = Book("Python OOPS Vol. 2", "Edcorner Learning")
print(book)

print() # ------------------------------------------------------------- #

print("End")