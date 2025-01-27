from products import Product
import pytest


def test_initialization():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.name == "Bose QuietComfort Earbuds"
    assert bose.price == 250
    assert bose.quantity == 500


def test_invalid_initialization():
    with pytest.raises(ValueError):
        assert Product("", price=1450, quantity=100) # empty name
        assert Product("MacBook Air M2", price=-1450, quantity=100) # negative price
        assert Product("MacBook Air M2", price=1450, quantity=-100) # negative quantity


def test_set_quantity_is_active():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    bose.set_quantity(-400)
    assert bose.is_active() == True


def test_buy():
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    assert mac.buy(50) == 72500.0
    assert mac.get_quantity() == 50
    assert mac.is_active() == True
    assert mac.buy(50) == 72500.0
    assert mac.is_active() == False


def test_buy_too_much():
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        assert mac.buy(101)




