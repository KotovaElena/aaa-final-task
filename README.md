# Pizza
This is the final project for the Python course at the Avito Analytics Academy.  

## Description

This is a pizza ordering interface created with click. 
There are two commands available in it: menu and order.
It is possible to order pizza of an affordable size from the available options. 
You can also choose the option of delivery or pickup.  

Pizzas:
* Margherita
* Pepperoni
* Hawaiian

Sizes:
* L
* XL

### Menu
To display the menu run this command in the terminal:  
`python pizza_cli.py menu`

### Order
To order pizza with delivery run this command in the terminal:  
`python pizza_cli.py order {pizza name} --delivery`  

To order pizza without delivery (pickup) run this command in the terminal:  
`python pizza_cli.py order {pizza name}`  

To choose the pizza size:    
`python pizza_cli.py order {pizza name} --size={pizza size}`

## Testing
Installing the package using pip:    
`pip install -U pytest-cov`

To run all tests with coverage measurement run this command in the terminal:   
`pytest --cov=pizza --cov=pizza_cli --cov=pizza_menu --cov=pizza_processes --cov`  

**Test results:**

* The tests are in the `tests` folder.
* File `results_testing.txt` contains the results of running tests with coverage.
* Code coverage by tests:
```
---------- coverage: platform win32, python 3.10.7-final-0 -----------  
Name                 Stmts   Miss  Cover  
----------------------------------------  
pizza.py                30      0   100%  
pizza_cli.py            26      2    92%  
pizza_menu.py           28      0   100%  
pizza_processes.py      23      0   100%  
----------------------------------------  
TOTAL                  107      2    98%  

============================= 21 passed in 0.31s ==============================
```



