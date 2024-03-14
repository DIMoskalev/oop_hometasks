from src.category import Category


def test_init_category(new_category):
    assert new_category.name == 'Смартфоны'
    assert new_category.description == 'Описание смартфонов'
    assert new_category.products[0]['name'] == "Samsung Galaxy C23 Ultra"
    assert Category.total_categories_amount == 1
    assert Category.total_uniq_products == 3
