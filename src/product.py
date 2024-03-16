class Product:
    """Класс конкретного товара в магазине"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f"\nНазвание: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Цена: {self.price}\n"
                f"Количество в наличии: {self.quantity}\n")
