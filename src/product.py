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

    @classmethod
    def add_new_product(cls, dict_with_product):
        name = dict_with_product['name']
        description = dict_with_product['description']
        price = dict_with_product['price']
        quantity = dict_with_product['quantity']
        return cls(name, description, price, quantity)

    @property
    def display_price(self):
        return self.price

    @display_price.setter
    def display_price(self, new_price):
        if new_price <= 0:
            print('Введена некорректная цена')
        else:
            self.price = new_price

    def __repr__(self):
        return (f"\nНазвание: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Цена: {self.price}\n"
                f"Количество в наличии: {self.quantity}\n")
