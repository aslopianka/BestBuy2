"""
This module defines the Promotion class, which represents a promotion in the store.
"""
from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions.
    """
    
    def __init__(self, name):
        """
        Initializes a new promotion.
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the promotion to the product and
        returns the discounted price after promotion was applied.
        """
        pass

class PercentDiscount(Promotion):
    """
    Applies a percentage discount to the product price.
    """
    def __init__(self, name, percent):
        """
        Initializes a percentage discount promotion.
        """
        super().__init__(name)
        self.discount_percentage = percent

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the percentage discount to the product and returns the total price.
        """
        single_discounted_price = product.price * (1 - self.discount_percentage / 100)
        return single_discounted_price * quantity


class ThirdOneFree(Promotion):
    """
    Promotion where every third item is free.
    """
    def __init__(self, name):
        """
        Initializes a 'Third One Free' promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """ Returns the total price of the product."""
        number_of_free_items = quantity // 3
        number_of_full_items = quantity - number_of_free_items

        return product.price * number_of_full_items


class SecondHalfPrice(Promotion):
    """
    Promotion where every second item is at half price.
    """
    def __init__(self, name):
        """
        Initializes a 'Second Half Price' promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the 'Second Half Price' promotion and returns the total price.
        """
        number_of_half_priced_items = quantity // 2
        number_of_full_priced_items = quantity - number_of_half_priced_items
        total_price = (product.price * number_of_full_priced_items) + ((product.price * 0.5) * number_of_half_priced_items)

        return total_price

