import turtle
from prettytable import PrettyTable
"""

my_screen = turtle.Screen()
my_screen.canvheight= 100
my_screen.canvwidth = 100


ferenc = turtle.Turtle()
ferenc.shape("turtle")
ferenc.color("black", "green")
ferenc.forward(100)


my_screen.exitonclick()
"""

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align  = "l"
print(table)
