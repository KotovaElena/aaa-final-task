from pizza_menu import PizzeriaMenu
from pizza import Margherita, Pepperoni, Hawaiian


def test_get_menu_pizzas() -> None:
    assert PizzeriaMenu().get_menu_pizzas() == {'Margherita': Margherita(),
                                                'Pepperoni': Pepperoni(),
                                                'Hawaiian': Hawaiian()}


def test_menu() -> None:
    assert PizzeriaMenu().__str__() == ' - Margherita 🧀: tomato sauce, mozzarella, tomatoes \n'\
                                       ' - Pepperoni 🍕: tomato sauce, mozzarella, pepperoni \n'\
                                       ' - Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples \n'
