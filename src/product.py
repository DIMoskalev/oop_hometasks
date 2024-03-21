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
        self.__price = price
        self.quantity = quantity

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

    def __repr__(self):
        return (f"\nНазвание: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Цена: {self.__price}\n"
                f"Количество в наличии: {self.quantity}\n")
