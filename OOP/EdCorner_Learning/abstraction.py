# learning abstraction

# Python ABC -> Abstraction Module for Abstract Class Syntax
from abc import ABC     # must import ABC in order to use abstraction

class Vehicle(ABC):     # inherits abstract class
    # abstract method (lack of definition -> not declared or remain empty)
    def no_of_wheels(self) -> None:
        pass

class Cycle(Vehicle):
    def no_of_wheels(self) -> None:     # provide definition for abstract method
        print("Cycle have 2 wheels.")

class Car(Vehicle):
    def no_of_wheels(self) -> None:     # provide definition for abstract method
        print("Car have 4 wheels.")

class HeavyTruck(Vehicle):
    def no_of_wheels(self) -> None:     # provide definition for abstract method
        print("Heavy Truck have 8 wheels.")

cycle = Cycle()
cycle.no_of_wheels()

car = Car()
car.no_of_wheels()

heavyTruck = HeavyTruck()
heavyTruck.no_of_wheels()