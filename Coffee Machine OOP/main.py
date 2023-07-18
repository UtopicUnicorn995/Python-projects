from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

for item in menu.menu:
    print(item.name)

is_on = True
while is_on:
    task = input(f"What would you like to order? {menu.get_items()}: ")
    if task == 'report':
        coffee_maker.report()
        money.report()
    else:
        find_drink = menu.find_drink(task)
        # coffee_maker.is_resource_sufficient(find_drink)
        # money.make_payment(menu.find_drink(task).cost)
        # coffee_maker.make_coffee(menu.find_drink(task))
        if coffee_maker.is_resource_sufficient(find_drink):
            if money.make_payment(menu.find_drink(task).cost):
                coffee_maker.make_coffee(menu.find_drink(task))
            else:
                is_on = False
        else:
            is_on = False


