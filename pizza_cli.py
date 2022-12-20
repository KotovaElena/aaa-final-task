import click
from pizza_menu import PizzeriaMenu
from pizza import PizzaSize
from pizza_processes import bake, deliver, pickup


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True, help='Delivery option')
@click.option('--size', default="L",
              type=click.Choice(list(PizzaSize.get_size().keys()), case_sensitive=False), help='Size option')
@click.argument('pizza', default='Margherita',
                type=click.Choice(list(PizzeriaMenu().get_menu_pizzas().keys()), case_sensitive=False), nargs=1)
def order(pizza: str, size: str, delivery: bool) -> None:
    """Bakes and delivers pizza"""
    pizzas_menu = PizzeriaMenu().get_menu_pizzas()
    pizza_exmp = pizzas_menu[pizza]
    pizza_exmp.size = size
    if delivery:
        print(bake(pizza_exmp), deliver(pizza_exmp), sep="\n")
    else:
        print(bake(pizza_exmp), pickup(pizza_exmp), sep="\n")


@cli.command()
@click.argument('menu_name', default='main', nargs=1)
def menu(menu_name: str) -> None:
    """Print menu"""
    print('MENU')
    if menu_name.lower() == 'main':
        print(PizzeriaMenu())


if __name__ == '__main__':
    cli()
