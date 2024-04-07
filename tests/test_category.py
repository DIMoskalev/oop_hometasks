import pytest

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
        'Xiaomi Redmi Note 11, 60000.0 руб. Остаток: 14 шт.'
    )


def test_str(new_category):
    assert new_category.__str__() == 'Смартфоны, количество продуктов: 27 шт.'


def test_len(new_category):
    assert new_category.__len__() == 27


def test_add_product_with_zero_quantity(new_category, product_with_zero_quantity):
    with pytest.raises(ValueError):
        new_category.add_product(product_with_zero_quantity)


def test_add_product_with_zero_quantity_text(new_category, product_with_zero_quantity):
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        new_category.add_product(product_with_zero_quantity)


def test_avg_price(new_category, new_category_empty):
    assert new_category.avg_price() == 150_000
    assert new_category_empty.avg_price() == 0
