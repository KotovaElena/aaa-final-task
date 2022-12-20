from pizza_processes import bake, deliver, pickup
from pizza import Margherita, Pepperoni, Hawaiian
import random
from unittest.mock import patch


def test_bake():
    if Margherita().size == 'L':
        assert bake.__wrapped__(Margherita()) in range(16, 34)
    if Margherita().size == 'XL':
        assert bake.__wrapped__(Margherita()) in range(18, 37)


def test_deliver():
    assert deliver.__wrapped__(Margherita()) in range(10, 21)


def test_pickup():
    assert pickup.__wrapped__(Pepperoni()) in range(5, 16)


def test_bake_with_decorator():
    with patch.object(random, 'randint', return_value=25):
        assert bake(Pepperoni()) == '🔪 Bake Pepperoni in 25 min ⌛ !'


def test_deliver_with_decorator():
    with patch.object(random, 'randint', return_value=15):
        assert deliver(Pepperoni()) == '🛵 Deliver Pepperoni in 15 min ⌛ !'


def test_pickup_with_decorator():
    with patch.object(random, 'randint', return_value=10):
        assert pickup(Hawaiian()) == '🏠 Pickup Hawaiian in 10 min ⌛ !'
