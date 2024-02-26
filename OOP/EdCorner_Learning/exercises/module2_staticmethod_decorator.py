""" 
    Module 2 Static Method - Decorator
"""

# import
import time
import uuid

# --------------------------------------------------------------------- #

class Container:
    def get_current_time() -> None:
        return time.strftime("%H:%M:%S", time.localtime())

    # converting get_convert_time() to static method
    get_current_time = staticmethod(get_current_time)

container = Container()
print(container.get_current_time())

print() # ------------------------------------------------------------- #

class ContainerTwo:
    @staticmethod
    def get_current_time() -> None:
        return time.strftime("%H:%M:%S", time.localtime())

containerTwo = ContainerTwo()
print(containerTwo.get_current_time())

print() # ------------------------------------------------------------- #

class Book:
    # constructor
    def __init__(self, title: str, author: str) -> None:
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]
    
book1 = Book("Python Object Oriented Programming Exercises Volume 2", "Edcorner Learning")
print(book1.__dict__.keys())
print(book1.__dict__)

print() # ------------------------------------------------------------- #

class BookTwo:
    # constructor
    def __init__(self, title: str, author: str) -> None:
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    # override __repr__ method, the default return is the name of the object and the memory location of the object
    def __repr__(self) -> str:
        return f"Book(title = '{self.title}', author = '{self.author}')."

    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]
    
bookTwo = BookTwo("Python Object Oriented Programming Exercises Volume 2", "Edcorner Learning")
print(bookTwo)

print() # ------------------------------------------------------------- #


