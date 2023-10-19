from item import Item

class Mouse(Item):
    pay_rate = 0.5
    all = []       
    def __init__(self, name: str, price: float, quantity = 0, broken_mouses = 0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments (assert 'statement', 'error message')
        assert broken_mouses >= 0, f"Broken Phones {broken_mouses} is not greater than or equal to zero!"

        # Assign to self object (below are instances attribute)
        self.broken_mouses = broken_mouses