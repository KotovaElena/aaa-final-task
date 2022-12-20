from pizza import Margherita, Pepperoni, Hawaiian, PizzaSize
import pytest


def test_comparison_equal() -> None:
    assert Pepperoni() == Pepperoni()


def test_comparison_unequal() -> None:
    assert Margherita() != Hawaiian()


def test_comparison_wrong() -> None:
    with pytest.raises(TypeError):
        Hawaiian().__eq__('wrong pizza')


def test_available_sizes() -> None:
    assert PizzaSize.get_size() == {'L': 1, 'XL': 2}


def test_dict_default_size() -> None:
    assert Pepperoni().dict() == {'tomato sauce': 100, 'mozzarella': 150, 'pepperoni': 300}


def test_dict_correct_size() -> None:
    assert Margherita().dict('XL') == {'tomato sauce': 200, 'mozzarella': 300, 'tomatoes': 400}


def test_dict_wrong_size() -> None:
    with pytest.raises(KeyError):
        assert Hawaiian().dict('M')
