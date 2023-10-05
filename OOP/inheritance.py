from assets.helper import *

# Create Parent Class
class VicePresident:
    def __init__(self, fname, lname, age):
        self.FirstName = fname
        self.LastName = lname
        self.Age = age
        print("This is Vice President " + self.FirstName)

    def printIdentity(self):
        print("Data Identity:\nFirstname: " + 
              self.FirstName + "\nLastname: " + 
              self.LastName + "\nAge: " + 
              f"{self.Age}")

x = VicePresident("Daniel", "Adi Pratama", 18)
x.printIdentity()

FreeSpace()

# Create Child Class (That overwrite the parent properties and function)
class Employee(VicePresident):
    def __init__(self, fname, lname, age):
        self.FirstName = fname
        self.LastName = lname
        self.Age = age
        print("This is Employee " + fname)

y = Employee("Budi", "Santoso", 25) # result: "This is Manager Tirza"
y.printIdentity()

FreeSpace()

# Create Child Class (That doesn't overwrite the parent properties and function)
class Manager(VicePresident):
    def __init__(self, fname, lname, age):
        VicePresident.__init__(self, fname, lname, age)

z = Manager("Tirza", "Nadya Wibowo", 18)
z.printIdentity()

FreeSpace()

# super() function
# make the child class inherit all the methods and properties from its parent
class Supervisor(VicePresident):
    def __init__(self, fname, lname, age, then, now):
        super().__init__(fname, lname, age)
        self.YearAccepted = then
        self.CurrentYear = now
        self.YearWork = self.CurrentYear - self.YearAccepted

    def printIdentity(self):
        return super().printIdentity()    
    
    def entrance(self):
        print("Currently Working in year " + f"{self.CurrentYear}")
        print("Got Accepted in year " + f"{self.YearAccepted}")
        if self.YearWork == 1 and not(self.YearWork < 1):
            print("Duration of Working: " + f"{self.YearWork}" + " year")
        else:
            print("Duration of Working: " + f"{self.YearWork}" + " years")

a = Supervisor("Bambang", "Nugroho", 23, 2021, 2023)
print(a.YearAccepted)
a.entrance()

FreeSpace()
