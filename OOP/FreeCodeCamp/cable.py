from item import Item

class Cable(Item):
    pay_rate = 0.5
    all = []       
    def __init__(self, name: str, price: float, quantity = 0, broken_cables = 0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments (assert 'statement', 'error message')
        assert broken_cables >= 0, f"Broken Cables {broken_cables} is not greater than or equal to zero!"

        # Assign to self object (below are instances attribute)
        self.broken_cables = broken_cables