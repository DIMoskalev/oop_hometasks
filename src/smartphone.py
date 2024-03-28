from src.product import Product


class Smartphone(Product):
    performance: str
    model: str
    amount_of_memory: float

    def __init__(self, name, description, price, quantity, color, performance, model, amount_of_memory):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.amount_of_memory = amount_of_memory
        if type(self) is Smartphone:
            print(super().__repr__())
