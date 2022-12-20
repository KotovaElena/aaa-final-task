class PizzaSize:
    """Contains possible sizes of pizzas"""
    _sizes = {
        'L': 1,
        'XL': 2
    }

    @staticmethod
    def get_size() -> dict[str, int]:
        """Static method to return pizzas sizes"""
        return PizzaSize._sizes


class BasePizza:
    """Base class for pizza with basic size and ingredients"""
    def __init__(self) -> None:
        self.size = 'L'
        self.ingredients = {
            'tomato sauce': 100,
            'mozzarella': 150
        }

    def dict(self, size: str = 'L') -> dict[str, int]:
        """Returns a pizza recipe with converted ingredient weights base on pizza size"""
        if size in PizzaSize.get_size().keys():
            coef = PizzaSize.get_size().get(size, 1)
            return {ingredient: cnt * coef for (ingredient, cnt) in self.ingredients.items()}
        raise KeyError('No such size')

    def __eq__(self, other) -> bool:
        """Pizza comparison"""
        if isinstance(other, BasePizza):
            return self.ingredients == other.ingredients
        raise TypeError('Compare two pizzas')


class Margherita(BasePizza):
    """Margherita pizza class"""
    def __init__(self) -> None:
        super().__init__()
        self.ingredients.update({'tomatoes': 200})


class Pepperoni(BasePizza):
    """Pepperoni pizza class"""
    def __init__(self) -> None:
        super().__init__()
        self.ingredients.update({'pepperoni': 300})


class Hawaiian(BasePizza):
    """Hawaiian pizza class"""
    def __init__(self) -> None:
        super().__init__()
        self.ingredients.update({'chicken': 120, 'pineapples': 80})
