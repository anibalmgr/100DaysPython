#  Create variable RECIPES.
RECIPES = {
    "espresso": {"water": 50, "coffee": 18, "dollars": 1.5},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "dollars": 2.5},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "dollars": 3.0}
}
# Create variable resources.
resources = {
    "water": 2000,
    "coffee": 250,
    "milk": 1000,
    "dollars": 0,
}

# report() return resources
def report():
    """Print the current resources in the coffee machine"""
    print(f'''
Coffee: {resources["coffee"]}gr.
Water: {resources["water"]}ml.
Milk: {resources["milk"]}ml.

Money: ${resources["dollars"]}
''')

# off() ends the while loop.
machine_on = True


def off():
    """return machine = False"""
    machine_on = False
    return machine_on

# check(recipe) returns True if resources are enough, false if not.


def choose(user_input):
    """Takes a string with the kind of coffee and return a dictionary with the selected coffee."""
    if user_input == "off" or user_input == "report":
        return user_input
    else:
        choice = RECIPES[user_input]
        return choice


def check(recipe):
    """Checks if the ingredients are enough in the machine resources, returns a boolean."""
    ingredients = True
    for resource in recipe:
        if resource != "dollars":
            if recipe[resource] > resources[resource]:
                print(f"Sorry, there's not enough {resource}")
                ingredients = False
    return ingredients

# coins() transform all coins into a unique value.


def add_money():
    """Takes different coins and returns the addition of the total"""
    quarter = int(input("quarters: "))
    dime = int(input("dimes: "))
    nickle = int(input("nickles: "))
    pennie = int(input("pennies: "))
    total = round(quarter * 0.25 + dime * 0.1 + nickle * 0.05 + pennie * 0.01, 2)
    return total

# payment() takes the final paid amount, check it against the coffee price, returns True id money is enough.

def payment(total, choice):
    """pass the total paid and return a boolean depending if the transaction was successful or not"""
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


# make() passes recipe, takes resources, return coffee

def make(coffee):
    """takes a king of coffee and return the resources left."""
    for ingredient in coffee:
        if ingredient != "dollars":
            resources[ingredient] -= coffee[ingredient]
    return resources

# machine()

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
