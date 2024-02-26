""" 
    Module 6 Miscelleanuoes Exercises
"""

import datetime
import math
import uuid

class Person:
    # constructor
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

people = [Person("Tom", 25), Person("John", 29), Person("Mike", 27), Person("Alice", 19)]
people.sort(key=lambda person: person.age)  # lambda = anonymous function (function that doesn't have nanme)
for person in people:
    print(f"{person.name} -> {person.age}")    

print() # --------------------------------------------------------------------- #

# Vector (x, y)
class Point:
    # constructor
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # formal representation of the object
    def __repr__(self) -> str:
        return f"(x={self.x},y={self.y})"

    # instance method
    def reset(self):
        self.x = 0
        self.y = 0
        
point = Point(4, 2)
print(point)
Point.reset(point)
print(point)

print() # --------------------------------------------------------------------- #

class Point:
    # constructor
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    # formal representation of the object
    def __repr__(self) -> str:
        return f"(x={self.x},y={self.y})"

    # instance method
    def reset(self):
        self.x = 0
        self.y = 0

    def calc_distance(self, other):
        xTotal = (other.x - self.x)**2
        yTotal = (other.y - self.y)**2
        total = math.sqrt(xTotal + yTotal)
        return total

p1 = Point(0, 3)
p2 = Point(4, 0)
print(p1.calc_distance(p2))

print() # --------------------------------------------------------------------- #

class Note:
    # constructor
    def __init__(self, content: str) -> None:
        self.content = content
        self.creationTime = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

note1 = Note("My First Note.")
note2 = Note("My Second Note.")

print(note1.__dict__)
print(note2.__dict__)

print() # --------------------------------------------------------------------- #

# case sensitive
class Note:
    # constructor
    def __init__(self, content: str) -> None:
        self.content = content
        self.creationTime = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Note(content='{self.content}')"

    # instance method
    def find(self, word: str) -> bool:
        return word in self.content

note1 = Note("Object Oriented Programming in Python.")
print(note1.find("python"))
print(note1.find("Python"))

print() # --------------------------------------------------------------------- #

# case insensitive
class Note:
    # constructor
    def __init__(self, content: str) -> None:
        self.content = content
        self.creationTime = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Note(content='{self.content}')"

    # instance method
    def find(self, word: str) -> bool:
        return word.lower() in self.content.lower()
    
note1 = Note("Object Oriented Programming in Python.")
print(note1.find("python"))
print(note1.find("Python"))

print() # --------------------------------------------------------------------- #

class Notebook:
    # constructor
    def __init__(self) -> None:
        self.notes = []

    # instance method
    def new_note(self, content) -> None:
        self.notes.append(Note(content))

notebook = Notebook()
notebook.new_note("My first note")
notebook.new_note("My second note")
print(notebook.notes)

print() # --------------------------------------------------------------------- #

# case insensitive
class Note:
    # constructor
    def __init__(self, content: str) -> None:
        self.content = content
        self.creationTime = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Note(content='{self.content}')"

    # instance method
    def find(self, word: str) -> bool:
        return word.lower() in self.content.lower()
    
class Notebook:
    # constructor
    def __init__(self) -> None:
        self.notes = []

    # instance method
    def new_note(self, content) -> None:
        self.notes.append(Note(content))

    def display_notes(self) -> list:
        for note in self.notes:
            print(note.content)

notebook = Notebook()
notebook.new_note("My first note")
notebook.new_note("My second note")
notebook.display_notes()

print() # --------------------------------------------------------------------- #

# case insensitive
class Note:
    # constructor
    def __init__(self, content: str) -> None:
        self.content = content
        self.creationTime = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Note(content='{self.content}')"

    # instance method
    def find(self, word: str) -> bool:
        return word.lower() in self.content.lower()
    
class Notebook:
    # constructor
    def __init__(self) -> None:
        self.notes = []

    # instance method
    def new_note(self, content) -> None:
        self.notes.append(Note(content))

    def display_notes(self) -> list:
        for note in self.notes:
            print(note.content)

    def search(self, word) -> list:
        return [note for note in self.notes if note.find(word)]

notebook = Notebook()
notebook.new_note("Big Data")
notebook.new_note("Data Science")
notebook.new_note("Machine Learning")
print(notebook.search("data"))
print(notebook.search("machine"))

print() # --------------------------------------------------------------------- #

class Client:
    # class attribute
    all_clients = []

    # constructor
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Client(name='{self.name}', email='{self.email}')"

client = Client("Tom", "sample@gmail.com")
client2 = Client("Donald", "sales@yahoo.com")
client3 = Client("Mike", "sales-contact@yahoo.com")
print(Client.all_clients)

print() # --------------------------------------------------------------------- #

class ClientList(list):
    def search_email(self, value):
        result = [client for client in self if value in client.email]
        return result

class Client:
    # class attribute
    all_clients = ClientList()

    # constructor
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Client(name='{self.name}', email='{self.email}')"

client = Client("Tom", "sample@gmail.com")
client2 = Client("Donald", "sales@yahoo.com")
client3 = Client("Mike", "sales-contact@yahoo.com")
client4 = Client("Lisa", "info@gmail.com")
print(Client.all_clients.search_email("sales"))
print(Client.all_clients.search_email("sample"))
print(Client.all_clients.search_email("info"))

print() # --------------------------------------------------------------------- #

# associated with previous code
print(Client.all_clients.search_email("gmail"))

print() # --------------------------------------------------------------------- #

class ClientList(list):
    def search_email(self, value):
        result = [client for client in self if value in client.email]
        return result

class Client:
    # class attribute
    all_clients = ClientList()

    # constructor
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Client.all_clients.append(self)

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Client(name='{self.name}', email='{self.email}')"

client = Client("Tom", "sample@gmail.com")
client2 = Client("Donald", "sales@yahoo.com")
client3 = Client("Mike", "sales-contact@yahoo.com")
client4 = Client("Lisa", "info@gmail.com")
print(Client.all_clients.search_email("sales"))

print() # --------------------------------------------------------------------- #

# associated with previous code
result = [client.name for client in Client.all_clients.search_email("sales")]
print(result)

print() # --------------------------------------------------------------------- #

class CustomDict(dict):
    # instance method
    def is_any_str_value(self) -> bool:
        for key in self:
            if isinstance(self[key], str):
                return True
        return False    

red = CustomDict(flag="red", test="easy")
number = CustomDict(number=200)
print(red.is_any_str_value())
print(number.is_any_str_value())

print() # --------------------------------------------------------------------- #

class StringListOnly(list):
    # instance method
    def append(self, string) -> None:
        if not isinstance(string, str):
            # raise TypeError("Only objects of type str can be added to the list.")
            print(TypeError("Only objects of type str can be added to the list."))
        super().append(string)

stringList = StringListOnly()   # stringList is now a list
stringList.append("Data")
stringList.append("Science")
print(stringList)
stringList.append(400)

print() # --------------------------------------------------------------------- #

class StringListOnly(list):
    # instance method
    def append(self, string) -> None:
        if not isinstance(string, str):
            # raise TypeError("Only objects of type str can be added to the list.")
            print(TypeError("Only objects of type str can be added to the list."))
        super().append(string.lower())

stringList = StringListOnly()   # stringList is now a list
stringList.append("Data")
stringList.append("Science")
stringList.append("Machine Learning")
print(stringList)

print() # --------------------------------------------------------------------- #

class Product:
    # constructor
    def __init__(self, product_name, price) -> None:
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Product(product_name='{self.product_name}', price='{self.price}')"

    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1][:6])

class Warehouse:
    # constructor
    def __init__(self) -> None:
        self.products = []

warehouse = Warehouse()
print(warehouse.products)

print() # --------------------------------------------------------------------- #

class Product:
    # constructor
    def __init__(self, product_name: str, price: int) -> None:
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Product(product_name='{self.product_name}', price='{self.price}')"

    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]

class Warehouse:
    # constructor
    def __init__(self) -> None:
        self.products = []

    # instance method
    def add_product(self, product_name: str, price: int) -> None:
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))

warehouse = Warehouse()
warehouse.add_product("Laptop", 3900)
warehouse.add_product("Mobile Phone", 1990)
warehouse.add_product("Mobile Phone", 1990)     # check if the filtering works
print(warehouse.products)

print() # --------------------------------------------------------------------- #

class Product:
    # constructor
    def __init__(self, product_name: str, price: int) -> None:
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Product(product_name='{self.product_name}', price='{self.price}')"
        
    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]

class Warehouse:
    # constructor
    def __init__(self) -> None:
        self.products = []

    # instance method
    def add_product(self, product_name: str, price: int) -> None:
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)

warehouse = Warehouse()
warehouse.add_product("Laptop", 3900)
warehouse.add_product("Mobile Phone", 1990)
warehouse.add_product("Camera", 2990)

print("Before removing Mobile Phone")
print(warehouse.products)   
print("After removing Mobile Phone")
warehouse.remove_product("Mobile Phone")
print(warehouse.products)   

print() # --------------------------------------------------------------------- #

class Product:
    # constructor
    def __init__(self, product_name: str, price: int) -> None:
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Product(product_name='{self.product_name}', price='{self.price}')"

    # informal representation of the object
    def __str__(self) -> str:
        return f"Product Name: {self.product_name} | {self.price}"
        
    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]

class Warehouse:
    # constructor
    def __init__(self) -> None:
        self.products = []

    # instance method
    def add_product(self, product_name: str, price: int) -> None:
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)

product = Product("Mobile Phone", 1990)
print(product)

print() # --------------------------------------------------------------------- #

class Product:
    # constructor
    def __init__(self, product_name: str, price: int) -> None:
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Product(product_name='{self.product_name}', price='{self.price}')"

    # informal representation of the object
    def __str__(self) -> str:
        return f"Product Name: {self.product_name} | {self.price}"
        
    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]

class Warehouse:
    # constructor
    def __init__(self) -> None:
        self.products = []

    # instance method
    def add_product(self, product_name: str, price: int) -> None:
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)

    def display_products(self):
        for product in self.products:
            print(product)

warehouse = Warehouse()
warehouse.add_product("Laptop", 3900)
warehouse.add_product("Mobile Phone", 1990)
warehouse.add_product("Camera", 2900)
warehouse.display_products()

print() # --------------------------------------------------------------------- #

class Product:
    # constructor
    def __init__(self, product_name: str, price: int) -> None:
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Product(product_name='{self.product_name}', price='{self.price}')"

    # informal representation of the object
    def __str__(self) -> str:
        return f"Product Name: {self.product_name} | {self.price}"
        
    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]

class Warehouse:
    # constructor
    def __init__(self) -> None:
        self.products = []

    # instance method
    def add_product(self, product_name: str, price: int) -> None:
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)

    def display_products(self):
        for product in self.products:
            print(f'Product ID: {product.product_id} | Product name: '
                    f'{product.product_name} | Price: {product.price}')
    
    def sort_by_price(self, ascending=True):
        return sorted(self.products, key=lambda product: product.price, reverse = not ascending)
    
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)

print("Ascending order:")
for product in warehouse.sort_by_price():
    print(product)
print("Descending order:")
for product in warehouse.sort_by_price(False):
    print(product)

print() # --------------------------------------------------------------------- #

class Product:
    # constructor
    def __init__(self, product_name: str, price: int) -> None:
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    # formal representation of the object
    def __repr__(self) -> str:
        return f"Product(product_name='{self.product_name}', price='{self.price}')"

    # informal representation of the object
    def __str__(self) -> str:
        return f"Product Name: {self.product_name} | {self.price}"
        
    @staticmethod
    def get_id() -> str:
        return str(uuid.uuid4().fields[-1])[:6]

class Warehouse:
    # constructor
    def __init__(self) -> None:
        self.products = []

    # instance method
    def add_product(self, product_name: str, price: int) -> None:
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name: str) -> None:
        for product in self.products:
            if product.product_name == product_name:
                self.products.remove(product)

    def display_products(self) -> None:
        for product in self.products:
            print(f'Product ID: {product.product_id} | Product name: '
                    f'{product.product_name} | Price: {product.price}')
    
    def sort_by_price(self, ascending=True) -> list:
        return sorted(self.products, key=lambda product: product.price, reverse = not ascending)
    
    def search_product(self, query: str) -> list:
        return [product for product in self.products 
                if query.lower() in product.product_name.lower()]
    
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
print(warehouse.search_product('M'))