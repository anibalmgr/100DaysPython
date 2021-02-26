from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

machine_on = True


while machine_on == True:
    choice_name = input(f"Which coffee would you like today? {menu.get_items()}: ")
    if choice_name == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    elif choice_name == "off":
        machine_on = False
    else:
        drink = menu.find_drink(choice_name)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"Your {drink.name} is {drink.cost}: ")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            input("Press any key to order again")
        else:
            input("press any key to start again")

