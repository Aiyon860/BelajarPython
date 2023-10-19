from item import Item

class Laptop(Item):
    pay_rate = 0.7
    all = []       
    def __init__(self, name: str, price: float, quantity = 0, broken_laptops = 0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments (assert 'statement', 'error message')
        assert broken_laptops >= 0, f"Broken Laptop {broken_laptops} is not greater than or equal to zero!"

        # Assign to self object (below are instances attribute)
        self.broken_laptops = broken_laptops 