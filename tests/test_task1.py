import pytest

from src.task1 import Category, Product


@pytest.fixture()
def new_category():
    return Category('Смартфоны',
                    'Описание смартфонов',
                    [
                        {
                            "name": "Samsung Galaxy C23 Ultra",
                            "description": "256GB, Серый цвет, 200MP камера",
                            "price": 180000.0,
                            "quantity": 5
                        },
                        {
                            "name": "Iphone 15",
                            "description": "512GB, Gray space",
                            "price": 210000.0,
                            "quantity": 8
                        },
                        {
                            "name": "Xiaomi Redmi Note 11",
                            "description": "1024GB, Синий",
                            "price": 31000.0,
                            "quantity": 14
                        }
                    ])


@pytest.fixture()
def new_product():
    return Product("Samsung Galaxy C23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)


def test_init_category(new_category):
    assert new_category.name == 'Смартфоны'
    assert new_category.description == 'Описание смартфонов'
    assert new_category.products[0]['name'] == "Samsung Galaxy C23 Ultra"
    assert Category.total_categories_amount == 1
    assert Category.total_uniq_products == 3


def test_init_product(new_product):
    assert new_product.name == 'Samsung Galaxy C23 Ultra'
    assert new_product.description == '256GB, Серый цвет, 200MP камера'
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
