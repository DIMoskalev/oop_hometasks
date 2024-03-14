def test_init_product(new_product):
    assert new_product.name == 'Samsung Galaxy C23 Ultra'
    assert new_product.description == '256GB, Серый цвет, 200MP камера'
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
