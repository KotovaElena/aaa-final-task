from pizza import BasePizza, Margherita, Pepperoni, Hawaiian
from functools import wraps
from typing import Callable


class EmojiMixin:
    """Replaces the name of the pizza in the menu with the name with an emoji"""
    ICON = {
        'Margherita': '🧀',
        'Pepperoni': '🍕',
        'Hawaiian': '🍍',
    }

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__str__ = cls._replace_str(cls.__str__)

    @classmethod
    def _replace_str(cls, func: Callable) -> Callable:
        """Decorator that replaces the __str__ function"""
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            text: str = func(*args, **kwargs)
            for word, emoj in cls.ICON.items():
                if word in PizzeriaMenu().pizzas.keys():
                    text = text.replace(word, f'{word} {emoj}')
            return text
        return wrapper


class PizzeriaMenu(EmojiMixin):
    """Pizza menu class"""
    def __init__(self) -> None:
        self.pizzas = {'Margherita': Margherita(),
                       'Pepperoni': Pepperoni(),
                       'Hawaiian': Hawaiian()}

    def get_menu_pizzas(self) -> dict[str, BasePizza]:
        """Returns pizzas from the menu"""
        return self.pizzas

    def __str__(self) -> str:
        """Returns menu"""
        menu = ''
        for key, value in self.pizzas.items():
            menu += f' - {key}: {", ".join(list(value.ingredients.keys()))} \n'
        return menu
