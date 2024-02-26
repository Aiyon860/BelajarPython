""" 
    Module 4 Inheritance
"""

print("Start")

print() # --------------------------------------------------------------------- #

class Container:
    pass

class PlasticContainer(Container):
    pass

class MetalContainer(Container):
    pass

class CustomContainer:
    pass

print(issubclass(PlasticContainer, Container))
print(issubclass(MetalContainer, Container))
print(issubclass(CustomContainer, Container))

print() # --------------------------------------------------------------------- #

class Vehicle:
    # constructor
    def __init__(self, category=None) -> None:
        self.category = category if category else "Land Vehicle"

    # return the formal representation of the object
    def __repr__(self) -> str:
        return f"Vehicle(category='{self.category}')"

class LandVehicle(Vehicle):
    # return the formal representation of the object
    def __repr__(self) -> str:
        return f"LandVehicle(cateogry='{self.category}')"

class AirVehicle(Vehicle):
    # constructor
    def __init__(self, category=None) -> None:
        self.category = category if category else "Air Vehicle"

    # return the formal representation of the object
    def __repr__(self) -> str:
        return f"AirVehicle(category='{self.category}')"

instances = [Vehicle(), LandVehicle(), AirVehicle()]
for instance in instances:
    print(instance)

print() # --------------------------------------------------------------------- #

class Vehicle:
    # constructor
    def __init__(self, category=None) -> None:
        self.category = category if category else "Land Vehicle"

    # return the formal representation of the object
    def __repr__(self) -> str:
        return f"Vehicle(category='{self.category}')"
    
    # instance method
    # display the class name along with the value of category attribute
    def display_info(self):
        return f"{self.__class__.__name__} -> {self.category}"

class LandVehicle(Vehicle):
    # return the formal representation of the object
    def __repr__(self) -> str:
        return f"LandVehicle(category='{self.category}')"

class AirVehicle(Vehicle):
    # constructor
    def __init__(self, category=None) -> None:
        self.category = category if category else "Air Vehicle"

    # return the formal representation of the object
    def __repr__(self) -> str:
        return f"AirVehicle(category='{self.category}')"

vehicles = [Vehicle(), LandVehicle(), AirVehicle()]
for vehicle in vehicles:
    print(vehicle.display_info())

print() # --------------------------------------------------------------------- #

class Vehicle:
    # constructor
    def __init__(self, brand: str, color: str, year: int) -> None:
        self.brand = brand
        self.color = color
        self.year = year

class Car(Vehicle):
    # override constructor
    def __init__(self, brand: str, color: str, year: int, horsepower: int) -> None:
        self.brand = brand
        self.color = color
        self.year = year
        self.horsepower = horsepower

car1 = Vehicle("BMW", "Red", 2020)
car2 = Car("BMW", "Red", 2020, 300)

print(car1.__dict__)
print(car2.__dict__)

print() # --------------------------------------------------------------------- #

class Vehicle:
    # constructor
    def __init__(self, brand: str, color: str, year: int) -> None:
        self.brand = brand
        self.color = color
        self.year = year

    # display instance attribute and their values
    def display_attrs(self) -> None:
        for attr, value in self.__dict__.items():
            print(f"{attr} -> {value}")

class Car(Vehicle):
    # override constructor
    def __init__(self, brand: str, color: str, year: int, horsepower: int) -> None:
        super().__init__(brand, color, year)
        self.horsepower = horsepower

car1 = Vehicle("Opel", "Black", 2018)
car2 = Car("Mclaren", "Orange", 2015, 450)

car1.display_attrs()
car2.display_attrs()

print() # --------------------------------------------------------------------- #

class Vehicle:
    # constructor
    def __init__(self, brand: str, color: str, year: int) -> None:
        self.brand = brand
        self.color = color
        self.year = year

    # display instance attribute and their values
    def display_attrs(self) -> None:
        for attr, value in self.__dict__.items():
            print(f"{attr} -> {value}")

class Car(Vehicle):
    # override constructor
    def __init__(self, brand: str, color: str, year: int, horsepower: int) -> None:
        super().__init__(brand, color, year)
        self.horsepower = horsepower

    # override the display instance method
    def display_attrs(self) -> None:
        print(f"Calling from class: {self.__class__.__name__}")
        super().display_attrs()

car1 = Car("Honda", "Black", 2010, 200)
car1.display_attrs()

print() # --------------------------------------------------------------------- #

class Container:
    pass

class TemperatureControlledContainer(Container):
    pass

class RefrigeratedContainer(TemperatureControlledContainer):
    pass

print(issubclass(TemperatureControlledContainer, Container));
print(issubclass(RefrigeratedContainer, TemperatureControlledContainer));
print(issubclass(RefrigeratedContainer, Container));

print() # --------------------------------------------------------------------- #

class Container:
    category = 'general purpose'

class TemperatureControlledContainer(Container):
    temp_range = (-25.0, 25.0)

class RefrigeratedContainer(TemperatureControlledContainer):
    temp_range = (-25.0, 5.0)

print(getattr(Container, 'category'))
print(getattr(TemperatureControlledContainer, 'temp_range'))
print(getattr(RefrigeratedContainer, 'temp_range'))

print() # --------------------------------------------------------------------- #

class Person:
    # constructor
    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname;
        self.lastname = lastname;
        self.age = age;

class Department:
    pass

class Worker(Person, Department):
    pass

worker = Worker("John", "Doe", 35)
print(worker.__dict__)

print() # --------------------------------------------------------------------- #

class Person:
    # constructor
    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname;
        self.lastname = lastname;
        self.age = age;

class Department:
    # constructor
    def __init__(self, deptname: str, short_dept_name: str) -> None:
        self.deptname = deptname
        self.short_dept_name = short_dept_name

class Worker(Person, Department):
    pass

department = Department("Information Technology", "IT")
print(department.__dict__)

print() # --------------------------------------------------------------------- #

class Person:
    # constructor
    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname;
        self.lastname = lastname;
        self.age = age;

class Department:
    # constructor
    def __init__(self, deptname: str, short_dept_name: str) -> None:
        self.deptname = deptname
        self.short_dept_name = short_dept_name

class Worker(Person, Department):
    # constructor
    def __init__(self, firstname: str, lastname: str, age: int, deptname: str, short_dept_name: str) -> None:
        Person.__init__(self, firstname, lastname, age)
        Department.__init__(self, deptname, short_dept_name)

worker = Worker("John", "Doe", 30, "Information Technology", "IT")
print(worker.__dict__)

print() # --------------------------------------------------------------------- #

# associated with previous code
print(Worker.mro())
