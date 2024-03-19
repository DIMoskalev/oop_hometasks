from src.product import Product


def test_init_product(new_product):
    assert new_product.name == 'Samsung Galaxy C23 Ultra'
    assert new_product.description == '256GB, Серый цвет, 200MP камера'
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_add_new_product(dict_with_product):
    assert Product.add_new_product(dict_with_product).name == "Samsung Galaxy C23 Ultra"


def test_display_price(new_product):
    assert new_product.display_price == 180_000
    # assert new_product.display_price(1) == 'Введена некорректная цена'
    new_product.display_price = 100
    assert new_product.display_price == 100
    new_product.display_price = 0
    assert new_product.display_price == 100

