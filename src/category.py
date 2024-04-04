from src.product import Product


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
        for prod in products:
            if not isinstance(prod, Product):
                raise TypeError('Можно добавлять в список только продукт или его наследников')
        self.__products = products

        Category.total_categories_amount += 1
        Category.total_uniq_products = len(self.__products)

    def __str__(self):
        """Магический метод, который возвращает строковое отображение информации о категории,
        содержащее информацию о сумме единиц товара в ней"""
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        """Магический метод, который возвращает общее число всех продуктов конкретной категории на складе"""
        counter = 0
        for product in self.__products:
            counter += product.quantity
        return counter

    def add_product(self, new_product):
        """Метод, который принимает на вход объект товара и добавляет его в список"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.total_uniq_products += 1
        if new_product.quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')

    @property
    def display_products(self):
        """Геттер, который выводит список товаров в формате: 'Продукт, 80 руб. Остаток: 15 шт.'"""
        result = (
            f'{product.name}, {product.display_price} руб. Остаток: {product.quantity} шт.'
            for product in self.__products
        )
        return "\n".join(result)

    def avg_price(self):
        

    def __repr__(self):
        return (f"\nНазвание: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Товары: {self.__products}\n")
