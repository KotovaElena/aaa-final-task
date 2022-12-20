from pizza import BasePizza, PizzaSize
from typing import Callable
from functools import wraps
import random


def log(template: str) -> Callable:
    """Returns the name of the process, the pizza and
    the execution time of the process according to the template"""
    def outer_wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner_wrapper(pizza: BasePizza) -> str:
            result = func(pizza)
            name = pizza.__class__.__name__
            return template.format(func.__name__.capitalize(), name, result)
        return inner_wrapper
    return outer_wrapper


@log('🔪 {} {} in {} min ⌛ !')
def bake(pizza: BasePizza) -> int:
    """Bake pizza"""
    coef = 1 + PizzaSize.get_size().get(pizza.size, 1)/10
    return random.randint(int(15 * coef), int(30 * coef))


@log('🛵 {} {} in {} min ⌛ !')
def deliver(pizza: BasePizza) -> int:
    """Deliver pizza"""
    return random.randint(10, 20)


@log('🏠 {} {} in {} min ⌛ !')
def pickup(pizza: BasePizza) -> int:
    """Pickup pizza"""
    return random.randint(5, 15)
