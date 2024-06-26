from src.basic import Basic
from src.mixinlog import MixinLog


class Product(MixinLog, Basic):
    """Класс конкретного товара в магазине"""
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color):
        """Метод инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color
        if type(self) is Product:
            print(super().__repr__())

    def __str__(self):
        return f'{self.name}, {self.display_price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(other) is not type(self):
            raise TypeError('Можно складывать товары только из одинаковых классов продуктов')
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def add_new_product(cls, dict_with_product):
        """Метод создает товар и возвращает объект, который можно добавлять в список товаров"""
        return cls(**dict_with_product)

    @property
    def display_price(self):
        """Геттер, который отображает цену товара"""
        return self.__price

    @display_price.setter
    def display_price(self, new_price):
        """Сеттер, который задет новое значение цены и проверяет, что введена корректная цена (>0)"""
        if new_price <= 0:
            print('Введена некорректная цена')
        else:
            self.__price = new_price
