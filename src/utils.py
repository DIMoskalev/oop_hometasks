import json

from src.category import Category
from src.product import Product


def read_from_file_json(file_path):
    """
    Функция считывает данные из файла file_path и возвращает список с товарами
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def creating_category_objects(list_of_objects):
    """Функция создает экземпляры класса Category"""
    list_of_category = []
    for data in list_of_objects:
        category = Category(data['name'], data['description'], data['products'])
        list_of_category.append(category)
    return list_of_category

def creating_product_objects(list_of_objects):
    """Функция создает экземпляры класса Product"""
    list_of_products = []
    for data in list_of_objects:
        for prod in data['products']:
            product = Product(prod['name'], prod['description'], prod['price'], prod['quantity'])
            list_of_products.append(product)
    return list_of_products
