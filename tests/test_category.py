from src.category import Category
from src.product import Product


def test_init_category(new_category):
    assert new_category.name == 'Смартфоны'
    assert new_category.description == 'Описание смартфонов'
    assert Category.total_categories_amount == 1
    assert Category.total_uniq_products == 3


def test_add_product(new_category, new_product):
    new_category.add_product(new_product)
    assert Category.total_uniq_products == 4


def test_display_products(new_category):
    assert new_category.display_products == (
        'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
        'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
        'Xiaomi Redmi Note 11, 1000.0 руб. Остаток: 14 шт.'
    )


def test_str(new_category):
    assert new_category.__str__() == (
        'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
        'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
        'Xiaomi Redmi Note 11, 1000.0 руб. Остаток: 14 шт.'
    )


def test_len(new_category):
    assert new_category.__len__() == 'Смартфоны, количество продуктов: 3 шт.'
