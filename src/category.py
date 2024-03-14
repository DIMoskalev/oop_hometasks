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
