"""
This module defines the Product class, which represents a product in the store.
"""
import promotions

class Product:
    """
    Represents a product with a name, price, quantity, and active status.
    """
    def __init__(self, name, price, quantity):
        """
        Initializes a new product.
        Checks for valid input types and values.
        """

        if not isinstance(name, str):
            raise TypeError("Product name must be a string text.")
        if len(name.strip()) == 0:
            raise ValueError("Product name cannot be empty or just spaces.")

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number (integer or float).")
        if price < 0:
            raise ValueError("Price cannot be a negative value.")

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a whole integer number.")
        if quantity < 0:
            raise ValueError("Quantity cannot be a negative value.")


        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None


    def get_quantity(self):
        """
        Returns the current quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Updates the product quantity.
        """
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a whole integer number.")
        if quantity < 0:
            raise ValueError("Quantity cannot be a negative value.")

        self.quantity = quantity

        if self.quantity == 0:
            self.active = False
        else: self.active = True

    def is_active(self):
        """
        Returns True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Sets the product status to active.
        """
        if self.quantity == 0:
            raise ValueError('The quantity is too low to set this item active.')
        else:
            self.active = True

    def deactivate(self):
        """
        Sets the product status to inactive.
        """
        self.active = False

    def show(self):
        """
        Prints the product details.
        """
        promo_name = self.promotion.name if self.promotion else "None"
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Promotion: {promo_name}")

    def buy(self, quantity):
        """
        Processes a purchase of the product.
        Reduces quantity and returns total price (applying promotions if any).
        """
        if quantity > self.quantity:
            raise ValueError(f"Not enough quantity of {self.name} in stock.")

        self.set_quantity(self.quantity - quantity)

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity

    def get_promotion(self):
        """
        Returns the current promotion assigned to the product.
        """
        return self.promotion

    def set_promotion(self, promotion):
        """
        Sets a new promotion for the product.
        """
        self.promotion = promotion


class NonStockedProduct(Product):
    def __init__(self, name, price):
        """
        Initializes a new NonStockProduct.
        It inherits from Product but has a quantity of 0 and bypasses the 0quantity-active restriction.
        """
        super().__init__(name, price, quantity=0)
        self.active = True

    def activate(self):
        """Bypasses the 0-quantity restriction to activate the product."""
        self.active = True

    def set_quantity(self, quantity):
        """Prevents changing the quantity of a non-stock product."""
        self.quantity = 0
        self.active = True
        raise(ValueError("Quantity cannot be changed for non-stock products."))

    def buy(self, quantity):
        """Only returns the price of the product. Does not reduce the quantity."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity

    def show(self):
        """Prints the product details."""
        promo_name = self.promotion.name if self.promotion else "None"
        print(f"{self.name}, Price: ${self.price}, Quantity: Unlimited, Promotion: {promo_name}")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        """
        Initializes a new LimitedProduct.
        It inherits from Product but has a maximum variable.
        """
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """
        Processes a purchase of the product.
        Reduces quantity and returns the total price
        but only allows the maximum amount per order.
        """
        if quantity > self.maximum:
            raise ValueError(f"For this product the maximum number per order is {self.maximum}.")

        return super().buy(quantity)

    def show(self):
        """Prints the product details."""
        promo_name = self.promotion.name if self.promotion else "None"
        print(f"{self.name}, Price: ${self.price}, Limited to only {self.maximum} per order!, Promotion: {promo_name}")
