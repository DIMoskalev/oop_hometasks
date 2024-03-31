import os
import pytest
from config import ROOT_DIR
from src.category import Category
from src.product import Product
from src.smartphone import Smartphone

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
                                5,
                                "Серый"),
                        Product("Iphone 15",
                                "512GB, Gray space",
                                210000.0,
                                8,
                                "Gray space"),
                        Product("Xiaomi Redmi Note 11",
                                "1024GB, Синий",
                                1000.0,
                                14,
                                "Синий")
                    ])


@pytest.fixture()
def new_product():
    return Product("Samsung Galaxy C23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0,
                   5,
                   "Серый")


@pytest.fixture()
def dict_with_product():
    return {"name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
            "color": "Серый"}


@pytest.fixture()
def new_product2():
    return Product("Iphone 15",
                   "512GB, Gray space",
                   210000.0,
                   8,
                   "Gray space")


@pytest.fixture()
def smart():
    return Smartphone("Iphone 15",
                      "512GB, Gray space",
                      210000.0,
                      8,
                      "Gray space",
                      "Капец какая производительность",
                      "Четкая модель",
                      "Очень много")
