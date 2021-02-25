# TODO: 1. Create variable RECIPES.
RECIPES = {
    "espresso": {"water": 50, "coffee": 18, "dollars": 1.5},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "dollars": 2.5},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "dollars": 3.0}
}
# TODO: 2. Create variable resources.
resources = {
    "water": 2000,
    "coffee": 250,
    "milk": 1000,
    "dollars": 0,
}

# TODO: 3. report() return resources
def report():
    print(f'''
Coffee: {resources["coffee"]}gr.
Water: {resources["water"]}ml.
Milk: {resources["milk"]}ml.

Money: ${resources["dollars"]}
''')

# TODO: 8. off() ends the while loop.
machine_on = True


def off():
    machine_on = False
    return machine_on

# TODO: 4. check(recipe) returns True if resources are enough, false if not.


def choose(user_input):
    if user_input == "off" or user_input == "report":
        return user_input
    else:
        choice = RECIPES[user_input]
        return choice


def check(recipe):
    ingredients = True
    for resource in recipe:
        if resource != "dollars":
            if recipe[resource] > resources[resource]:
                print(f"Sorry, there's not enough {resource}")
                ingredients = False
    return ingredients

# TODO: 5. coins() transform all coins into a unique value.


def add_money():
    quarter = int(input("quarters: "))
    dime = int(input("dimes: "))
    nickle = int(input("nickles: "))
    pennie = int(input("pennies: "))
    total = round(quarter * 0.25 + dime * 0.1 + nickle * 0.05 + pennie * 0.01, 2)
    return total

# TODO: 6. payment() takes the final paid amount, check it against the coffee price, returns True id money is enough.


def payment(total, choice):
    if total < choice["dollars"]:
        print(f"total: {total} price: {choice['dollars']}")
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources["dollars"]+= choice["dollars"]
        if total > choice["dollars"]:
            change = round(total - choice["dollars"], 2)
            print(f"Your change is ${change}.")
        return True


# Todo: 7. make() passes recipe, takes resources, return coffee

def make(coffee):
    for ingredient in coffee:
        if ingredient != "dollars":
            resources[ingredient] -= coffee[ingredient]
    return resources

# Todo: 9. recharge() transform money in coffee, milk or water.

# TODO: 10. machine()

def machine():
    machine_on = True
    while machine_on:
        global resources
        print("Welcome to the coffee machine")
        user_input = input("What would you like? (espresso/latte/cappuccino) :").lower()
        choice = choose(user_input)
        if choice == "off":
            return off()
        if choice == "report":
            return report()
        if check(choice):
            total = add_money()
            if payment(total, choice):
                resources = make(choice)
                print(f"Thank you, enjoy your {user_input}")
        report()




machine()
