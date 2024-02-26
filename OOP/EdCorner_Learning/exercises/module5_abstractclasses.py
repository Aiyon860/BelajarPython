""" 
    Module 5 Abstract Classes
"""


from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Figure):
    # constructor
    def __init__(self, a) -> None:
        self.a = a

    # implement 'area' method
    def area(self) -> int:
        return self.a * self.a
    
""" try:
    Figure()    # can't instantiate abstract class 'Figure'
except TypeError as Error:
    print(Error) """

print() # --------------------------------------------------------------------- #

class Figure(ABC):
    @abstractmethod
    def area(self) -> int:
        pass

    @abstractmethod
    def perimeter(self) -> int:
        pass

class Square(Figure):
    # constructor
    def __init__(self, a) -> None:
        self.a = a

    # implement 'area' method
    def area(self) -> int:
        return self.a * self.a
    
    # implement 'perimeter' method
    def perimeter(self) -> int:
        return 4 * self.a 

square = Square(10)
print(f"Square Area: {square.area()}\nSquare Perimeter: {square.perimeter()}")

print() # --------------------------------------------------------------------- #

class TaxPayer(ABC):
    # constructor
    def __init__(self, salary: int) -> None:
        self.salary = salary

    @abstractmethod
    def calculate_tax(self) -> int:
        pass

class StudentTaxPayer(TaxPayer):
    # implement calculate_tax
    def calculate_tax(self) -> int:
        return int(0.15 * self.salary)

student = StudentTaxPayer(40000)
print(f"Student Salary Tax: {student.calculate_tax()}")

print() # --------------------------------------------------------------------- #

class TaxPayer(ABC):
    # constructor
    def __init__(self, salary: int) -> None:
        self.salary = salary

    @abstractmethod
    def calculate_tax(self) -> int:
        pass

class DisabledTaxPayer(TaxPayer):
    def calculate_tax(self) -> int:
        salary_tax = int(0.12 * self.salary)
        return min(salary_tax, 5000)
    
disabled = DisabledTaxPayer(50000)
disabled2 = DisabledTaxPayer(10000)

print(disabled.calculate_tax())
print(disabled2.calculate_tax())

print() # --------------------------------------------------------------------- #

class TaxPayer(ABC):
    # constructor
    def __init__(self, salary: int) -> None:
        self.salary = salary

    @abstractmethod
    def calculate_tax(self) -> int:
        pass

class WorkerTaxPayer(TaxPayer):
    def calculate_tax(self) -> int:
        if self.salary < 80_000:
            return int(0.17 * self.salary)
        else:
            return int(80_000 * 0.17 + (self.salary - 80_000) * 0.32)

worker = WorkerTaxPayer(70_000)
worker2 = WorkerTaxPayer(95_000)

print(worker.calculate_tax())
print(worker2.calculate_tax())

print() # --------------------------------------------------------------------- #

class TaxPayer(ABC):
    # class variable
    tax_payers = []

    # constructor
    def __init__(self, salary: int) -> None:
        self.salary = salary
        TaxPayer.tax_payers.append(self)

    @abstractmethod
    def calculate_tax(self) -> int:
        pass

    @staticmethod
    def loop_calculate_tax() -> None:
        for tax_payer in TaxPayer.tax_payers:
            print(tax_payer.calculate_tax())

class StudentTaxPayer(TaxPayer):
    # implement calculate_tax
    def calculate_tax(self) -> int:
        tax = int(0.15 * self.salary)
        return tax

class DisabledTaxPayer(TaxPayer):
    def calculate_tax(self) -> int:
        tax = int(0.12 * self.salary)
        return min(tax, 5000)

class WorkerTaxPayer(TaxPayer):
    def calculate_tax(self) -> int:
        if self.salary < 80_000:
            tax = int(0.17 * self.salary)
            return tax
        else:
            tax = int(80_000 * 0.17 + (self.salary - 80_000) * 0.32)
            return tax

student = StudentTaxPayer(50_000)
disabled = DisabledTaxPayer(70_000)
worker = WorkerTaxPayer(68_000)
worker2 = WorkerTaxPayer(120_000)

TaxPayer.loop_calculate_tax()