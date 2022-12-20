from pizza_cli import menu, order
import random
from click.testing import CliRunner
from unittest.mock import patch


def test_menu() -> None:
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.exit_code == 0
    assert result.output == ('MENU\n'
                             ' - Margherita 🧀: tomato sauce, mozzarella, tomatoes \n'
                             ' - Pepperoni 🍕: tomato sauce, mozzarella, pepperoni \n'
                             ' - Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples \n'
                             '\n')


def test_default_order() -> None:
    with patch.object(random, 'randint', return_value=20):
        runner = CliRunner()
        result = runner.invoke(order)
        assert result.exit_code == 0
        assert result.output == ('🔪 Bake Margherita in 20 min ⌛ !\n'
                                 '🏠 Pickup Margherita in 20 min ⌛ !\n')


def test_order_delivery() -> None:
    with patch.object(random, 'randint', return_value=10):
        runner = CliRunner()
        result = runner.invoke(order, ['Pepperoni', '--size=L', '--delivery'])
        assert result.exit_code == 0
        assert result.output == ('🔪 Bake Pepperoni in 10 min ⌛ !\n'
                                 '🛵 Deliver Pepperoni in 10 min ⌛ !\n')


def test_order_pickup() -> None:
    with patch.object(random, 'randint', return_value=10):
        runner = CliRunner()
        result = runner.invoke(order, ['Pepperoni', '--size=XL'])
        assert result.exit_code == 0
        assert result.output == ('🔪 Bake Pepperoni in 10 min ⌛ !\n'
                                 '🏠 Pickup Pepperoni in 10 min ⌛ !\n')


def test_wrong_pizza() -> None:
    with patch.object(random, 'randint', return_value=10):
        runner = CliRunner()
        result = runner.invoke(order, ['Senorita', '--size=L'])
        assert result.exit_code == 2
        assert result.output == ('Usage: order [OPTIONS] [[Margherita|Pepperoni|Hawaiian]]\n'
                                 "Try 'order --help' for help.\n"
                                 '\n'
                                 "Error: Invalid value for '[[Margherita|Pepperoni|Hawaiian]]': 'Senorita' is "
                                 "not one of 'Margherita', 'Pepperoni', 'Hawaiian'.\n")


def test_wrong_size() -> None:
    with patch.object(random, 'randint', return_value=10):
        runner = CliRunner()
        result = runner.invoke(order, ['Pepperoni', '--size=M'])
        assert result.exit_code == 2
        assert result.output == ('Usage: order [OPTIONS] [[Margherita|Pepperoni|Hawaiian]]\n'
                                 "Try 'order --help' for help.\n"
                                 '\n'
                                 "Error: Invalid value for '--size': 'M' is "
                                 "not one of 'L', 'XL'.\n")
