import os
import pytest
from config import ROOT_DIR
from src.category import Category
from src.product import Product

OPERATIONS_PATH = os.path.join(ROOT_DIR, 'src', 'products.json')


@pytest.fixture
def list_json():
    return OPERATIONS_PATH


@pytest.fixture()
def new_category():
    return Category('Смартфоны',
                    'Описание смартфонов',
                    [
                        Product("Samsung Galaxy C23 Ultra",
                                "256GB, Серый цвет, 200MP камера",
                                180000.0,
                                5),
                        Product("Iphone 15",
                                "512GB, Gray space",
                                210000.0,
                                8),
                        Product("Xiaomi Redmi Note 11",
                                "1024GB, Синий",
                                1000.0,
                                14)
                    ])


@pytest.fixture()
def new_product():
    return Product("Samsung Galaxy C23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5)
