import pytest

from products import Product


#Test that creating a normal product works.


def test_product_creation():
    product = Product(name="MacBook Pro", price=1999.99, quantity=5)

    assert product.name == "MacBook Pro"
    assert product.price == 1999.99
    assert product.quantity == 5
    assert product.is_active() is True


def test_product_invalid_details():
    # name
    with pytest.raises(TypeError, match="Product name must be a string text."):
        Product(name=123, price=10.0, quantity=5)
    with pytest.raises(ValueError, match="Product name cannot be empty or just spaces."):
        Product(name="   ", price=10.0, quantity=5)
    # price
    with pytest.raises(TypeError, match="Price must be a number \\(integer or float\\)."):
        Product(name="MacBook Air M2", price="10.0", quantity=5)
    with pytest.raises(ValueError, match="Price cannot be a negative value."):
        Product(name="MacBook Air M2", price=-10.0, quantity=5)
    # quantity
    with pytest.raises(TypeError, match="Quantity must be a whole integer number."):
        Product(name="MacBook Air M2", price=10.0, quantity=5.5)
    with pytest.raises(ValueError, match="Quantity cannot be a negative value."):
        Product(name="MacBook Air M2", price=10.0, quantity=-5)


def test_product_inactive_when_quantity_is_zero():
    empty_prod = Product("Sold Out Item", 5.0, 0)
    # Init with active = True, so we must deactivate first to test activation
    empty_prod.deactivate()

    with pytest.raises(ValueError, match="The quantity is too low to set this item active."):
        empty_prod.activate()


def test_product_purchase():
    new_prod = Product("MacBook Air M2", 1000.0, 10)
    new_prod.buy(5)
    assert new_prod.quantity == 5
    assert new_prod.buy(5) == 5000.0

    with pytest.raises(ValueError, match="Not enough quantity of MacBook Air M2 in stock."):
        new_prod.buy(10)


def test_product_buy_too_much():
    new_prod = Product("MacBook Air M2", 1000.0, 10)
    with pytest.raises(ValueError, match="Not enough quantity of MacBook Air M2 in stock."):
        new_prod.buy(11)