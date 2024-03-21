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

    def __str__(self):
        """Магический метод, для строкового отображения продукта в формате: 'Продукт, 80 руб. Остаток: 15 шт.'"""
        result = (
            f'{product.name}, {product.display_price} руб. Остаток: {product.quantity} шт.'
            for product in self.__products
        )
        return "\n".join(result)

    def __len__(self):
        """Магический метод, который выводит общее число всех продуктов на складе"""
        return f'{self.name}, количество продуктов: {len(self.__products)} шт.'

    def add_product(self, new_product):
        """Метод, который принимает на вход объект товара и добавляет его в список"""
        self.__products.append(new_product)
        Category.total_uniq_products += 1

    @property
    def display_products(self):
        """Геттер, который выводит список товаров в формате: 'Продукт, 80 руб. Остаток: 15 шт.'"""
        result = (
            f'{product.name}, {product.display_price} руб. Остаток: {product.quantity} шт.'
            for product in self.__products
        )
        return "\n".join(result)

    def __repr__(self):
        return (f"\nНазвание: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Товары: {self.__products}\n")
