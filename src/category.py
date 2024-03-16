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
        self.__products = products

        Category.total_categories_amount += 1
        Category.total_uniq_products = len(self.__products)

    def __repr__(self):
        return (f"\nНазвание: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Товары: {self.__products}\n")

    def add_product(self, new_product):
        self.__products.append(new_product)

    @property
    def display_products(self):
        list_of_products = ''
        for product in self.__products:
            list_of_products += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return list_of_products


# tov = Category('Something', 'description', [Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#       # {
#       #   "name": "Samsung Galaxy C23 Ultra",
#       #   "description": "256GB, Серый цвет, 200MP камера",
#       #   "price": 180000.0,
#       #   "quantity": 5
#       # },
#       # {
#       #   "name": "Iphone 15",
#       #   "description": "512GB, Gray space",
#       #   "price": 210000.0,
#       #   "quantity": 8
#       # },
#       # {
#       #   "name": "Xiaomi Redmi Note 11",
#       #   "description": "1024GB, Синий",
#       #   "price": 31000.0,
#       #   "quantity": 14
#       # }
#     # ])
#                ])
# print(Category.total_categories_amount)
# print(tov)
# print(tov.display_products)
#
