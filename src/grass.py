from src.mixinlog import MixinLog
from src.product import Product


class Grass(MixinLog, Product):

    manufacturer_country: str
    germination_period: str

    def __init__(self, name, description, price, quantity, color, manufacturer_country, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        if type(self) is Grass:
            print(super().__repr__())
