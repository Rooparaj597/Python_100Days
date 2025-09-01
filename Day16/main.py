# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(200)
#
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()

#import a package prettytable to print the table
from prettytable import PrettyTable

#create a object 
table = PrettyTable()

# to add column in the table use add_column syntax
table.add_column("Pokemons name", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Metapod", "Bug"])
table.align = "l"
print(table)