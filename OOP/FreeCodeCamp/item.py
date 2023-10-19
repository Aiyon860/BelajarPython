import csv

class Item:
    pay_rate = 0.8  # Class Attribute
    all = []        # WAJIB PAKE 'all'
    # when we give default value to the parameter, the argument value type must match with the default value type given in parameter (look at quantity = 0)
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert type(price) == float
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert type(quantity) == int
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object (below are instances attribute)
        self.__name = name      # __ means that the attribute is private
        self.__price = price
        self.__quantity = quantity

        # Actions to Execute
        Item.all.append(self)

    ### GETTER AND SETTER
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        print(f"Getting a value: '{self.__name}'")
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise Exception("Cannot fill the name with null value!")
        elif value == ' ':
            raise Exception("Cannot fill the name with blank value!")
        elif len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
            print(f"Setting a value: '{self.__name}'")

    @property
    def price(self):
        print(f"Getting a value: '{self.__price}'")
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @price.setter
    def price(self, value):
        if value < 0:
            raise Exception("The price cannot under 0 !")
        else: 
            self.__price = value
            print("Getting a value: '{self.__price}'")

    @property
    def quantity(self):
        print(f"Getting a value: '{self.__quantity}'")
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise Exception("The quantity cannot under 0 !")
        else:
            self.__quantity = value
            print("Getting a value: '{self.__quantity}'")

    def counting_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('D:\ExpertProgrammer\Languages\Python\Belajar\OOP\FreeCodeCamp\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        # for instantiate instances
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Magic method to represent object, so we can avoid result such as memory address like 0x000001867AFFD750, etc
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.__quantity})"
    
    # Simulate Abstraction
    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone,
        We have {self.__name} {self.__quantity} times
        Regards, Daniel Aiyon
        """
    
    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
    
# Archive
""" # print(Item.__dict__)  # All the attributes for Class level
print(Item.pay_rate)    

Item1 = Item("Phone", 100, 5)
# print(Item1.__dict__)     # All the attributes for Instance level
Item1.apply_discount()      # Access pay_rate from Class level because there is no pay_rate attribute in instance level
print(Item1.price)

Item2 = Item("Laptop", 1000, 3)
Item2.pay_rate = 0.7
Item2.apply_discount()      # Access pay_rate from Instance level because there is pay_rate attribute in Instance level
print(Item2.price) 

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

#print(Item.all)     # to check if the instance is added to the 'all' list/array in class 'item'
for instance in Item.all:
    print(instance)

for instance in Item.all:                                                                                                                                                                      
    print(instance.name) 

Item.instantiate_from_csv()

print(Item.all) 

print(Item.is_integer(5))
print(Item.is_integer(5.0))
print(Item.is_integer(5.5)) """