# learning encapsulation
""" 
    Encapsulation is programming approach that ties the class'
    variable and method together and make them impossible for other classes or
    entities to access them.

    Encapsulation is used for security in OOP.
    Encapsulation protects the data/object/piece of informations from outer access
    from which people/entities don't have permission to access that data.
"""

# implement encapsulation by using Getter and Setter
class Library:
    def __init__(self, id: int, name: str) -> None:
        self.bookId = id
        self.bookName = name
    
    # setters method to set the book name
    def setBookName(self, newBookName) -> None:
        self.bookName = newBookName;

    # getters method to get the book name
    def getBookName(self) -> None:
        print(f"The name of book is {self.bookName}.")
    
    # getters method to get the book information
    def getBookInfo(self) -> None:
        print(f"The book id is {self.bookId} and book name is {self.bookName}.")

book = Library(101, "Crack your SQL Interview in One Day")
book.getBookName()
book.getBookInfo()
print()
book.setBookName("Crack your Python Django Interview Like a Pro")
book.getBookName()
book.getBookInfo()

print()

# Access Modifiers
""" 
    1. Private: only available to members of the class (double underscores)
    2. Public: can be accessed from any place outside of the class 
    3. Protected: only avaiable within the class and its subclasses (single underscore)
"""

class Employee:
    def __init__(self, name: str, employeeId: int, salary: int) -> None:
        self.name = name            # making employee name public
        self._empId = employeeId    # making employee ID protected
        self.__salary = salary      # making salary private

    def getSalary(self):
        print(f"The salary of Employee is {self.__salary}.")

employee1 = Employee("Daniel", 12345, 100_000)

print(f"The Employee's name is {employee1.name}")
print(f"The Employee's ID is {employee1._empId}")
# print(f"The Employee's salary is {employee1.__salary}") --> AttributeError: 'Employee' object has no attribute '__salary'
employee1.getSalary()   # access the employee's salary by calling this getter method
