# TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
from data import MENU, resources
resources['money'] = 0
is_power_on = True


def get_water(item):
    return item['ingredients']['water']


def get_coffee(item):
    return item['ingredients']['coffee']


def get_milk(item):
    return item['ingredients']['milk']


def get_cost(item):
    return item['cost']


def calculate_total(quarters, dimes, nickels, pennies):
    return ((quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1)) / 100


def solve_order(item):
    """"Calculates the new resources if successful"""
    # TODO: Process coins.
    print("Please insert coins")
    product_price = MENU[item]["cost"]
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = calculate_total(quarters, dimes, nickels, pennies)

    if total < product_price:
        print(f"Sorry you don't have enough money. here's your ${total} back")
    else:
        if item == 'espresso':
            resources["water"] -= MENU[item]["ingredients"]["water"]
            resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
            resources['money'] += MENU[item]['cost']
        else:
            resources["water"] -= MENU[item]["ingredients"]["water"]
            resources["milk"] -= MENU[item]["ingredients"]["milk"]
            resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
        # TODO: Check transaction successful?
        print("Transaction success")
        print(f"Here's your change of ${total - product_price}.")
# TODO: Make Coffee


while is_power_on:

    task = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: Turn off the Coffee Machine by entering “off” to the prompt.
    if task == 'off':
        is_power_on = False

# TODO: Print report.
    elif task == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

# TODO: Check resources sufficient?
    elif task == 'espresso':
        if get_water(MENU[task]) > resources["water"] and get_coffee(MENU[task]) > \
                resources["coffee"]:
            print("Sorry there is not enough water or coffee")
        elif get_water(MENU[task]) > resources["water"]:
            print("Sorry there is not enough water.")
        elif get_coffee(MENU[task]) > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            solve_order(task)

    elif task == 'latte':
        if get_water(MENU[task]) > resources["water"] and get_coffee(MENU[task]) > \
                resources["coffee"] and get_milk(MENU[task]) > resources["milk"]:
            print("Sorry there is not enough water, coffee or milk")
        elif get_water(MENU[task]) > resources["water"]:
            print("Sorry there is not enough water.")
        elif get_coffee(MENU[task]) > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        elif get_milk(MENU[task]) > resources["milk"]:
            print("Sorry there is not enough milk")
        else:
            solve_order(task)

    elif task == 'cappuccino':
        if get_water(MENU[task]) > resources["water"] and get_coffee(MENU[task]) > \
                resources["coffee"] and get_milk(MENU[task]) > resources["milk"]:
            print("Sorry there is not enough water, coffee or milk")
        elif get_water(MENU[task]) > resources["water"]:
            print("Sorry there is not enough water.")
        elif get_coffee(MENU[task]) > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        elif get_milk(MENU[task]) > resources["milk"]:
            print("Sorry there is not enough milk")
        else:
            solve_order(task)

    else:
        print("Sorry, what you entered is not in the options")
