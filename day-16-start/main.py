# import another_module
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
#
# timmy.speed(2)
# timmy.forward(600)
# timmy.color("coral")
# timmy.back(700)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Eladio", ["Sulio", "perop", "Escadio"])
table.align = "l"

print(table)