from data import *

actual_resources = resources
money = 0
is_machine_on = True


def user_select():
    user_selection_input = input("What would you like? (espresso/latte/cappuccino)\n")
    return user_selection_input


def print_status():
    print(
        f"Water: {actual_resources['water']}ml\nMilk: {actual_resources['milk']}ml\nCoffee: {actual_resources['coffee']}g\nMoney: ${money}\n")


def check_resources_for_drink(user_selection):
    drink_ingredients = MENU[user_selection]['ingredients']
    if actual_resources['water'] <= drink_ingredients['water']:
        return False
    elif actual_resources['milk'] <= drink_ingredients['milk']:
        return False
    elif actual_resources['coffee'] <= drink_ingredients['coffee']:
        return False
    else:
        return True


def print_not_enough_resources_error():
    print("Not enough resources available. Please select other drink.")


def update_money(machine_money, inserted_coins):
    return machine_money + inserted_coins


def insert_coins(user_selection):
    global money
    cost_ = MENU[user_selection]["cost"]
    print(f"Please, insert ${cost_}.")
    quarters = int(input("How many quarters would you like insert?\n"))
    dimes = int(input("How many dimes would you like insert?\n"))
    nickels = int(input("How many nickels would you like insert?\n"))
    pennies = int(input("How many pennies would you like insert?\n"))
    inserted_sum = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if inserted_sum >= cost_:
        money = update_money(money, cost_)
        if inserted_sum > cost_:
            print(f"You inserted ${inserted_sum}, change is ${round(inserted_sum - cost_, 2)}")
        return True
    else:
        print(f"You inserted ${inserted_sum}, but cost is ${cost_}")
        return False


def update_resources(user_selection):
    drink_ingredients = MENU[user_selection]['ingredients']
    actual_resources['water'] -= drink_ingredients['water']
    actual_resources['milk'] -= drink_ingredients['milk']
    actual_resources['coffee'] -= drink_ingredients['coffee']


def prepare_drink(user_selection):
    is_resources_enough = check_resources_for_drink(user_selection)
    if is_resources_enough:
        is_enough_money = insert_coins(user_selection)
        if is_enough_money:
            update_resources(user_selection)
            print(f"Here is your {user_selection}!")
    else:
        print_not_enough_resources_error()


while is_machine_on:
    user_selection = user_select()
    if user_selection == "off":
        is_machine_on = False
    elif user_selection == "status":
        print_status()
    else:
        prepare_drink(user_selection)
