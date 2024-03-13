class Category:
    """Класс категорий товаров в магазине"""
    total_categories_amount = 0
    total_uniq_products = 0
    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        """Метод инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.products = products

        Category.total_categories_amount += 1
        Category.total_uniq_products = len(self.products)


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


# product1 = Category('Книги', 'Большой сборник фантастики', ['Дюна', 'Темная башня','Косиног'])
# print(Category.total_categories_amount)
# print(Category.total_uniq_products)