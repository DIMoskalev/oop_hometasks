from src.product import Product


def test_init_product(new_product):
    assert new_product.name == 'Samsung Galaxy C23 Ultra'
    assert new_product.description == '256GB, Серый цвет, 200MP камера'
    assert new_product.display_price == 180000.0
    assert new_product.quantity == 5
    assert new_product.color == 'Серый'


def test_add_new_product(dict_with_product):
    assert Product.add_new_product(dict_with_product).name == "Samsung Galaxy C23 Ultra"
    assert Product.add_new_product(dict_with_product).color == "Серый"


def test_display_price(new_product):
    assert new_product.display_price == 180_000
    new_product.display_price = 100
    assert new_product.display_price == 100
    new_product.display_price = 0
    assert new_product.display_price == 100


def test_str(new_product, new_product2):
    assert new_product.__str__() == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert new_product2.__str__() == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'


def test_add(new_product, new_product2):
    assert new_product + new_product2 == 2580000.0


def test_repr(new_product):
    assert repr(new_product) == ("Создан объект Product(dict_values(['Samsung Galaxy C23 Ultra', '256GB, Серый "
                                 "цвет, 200MP камера', 180000.0, 5, 'Серый']))")
