from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the promotion to the product and
        returns the discounted price after promotion was applied.
        """
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.discount_percentage = percent

    def apply_promotion(self, product, quantity) -> float:
        single_discounted_price = product.price * (1 - self.discount_percentage / 100)
        return single_discounted_price * quantity


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """ Returns the total price of the product."""
        number_of_free_items = quantity // 3
        number_of_full_items = quantity - number_of_free_items

        return product.price * number_of_full_items


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        number_of_half_priced_items = quantity // 2
        number_of_full_priced_items = quantity - number_of_half_priced_items
        total_price = (product.price * number_of_full_priced_items) + ((product.price * 0.5) * number_of_half_priced_items)

        return total_price

