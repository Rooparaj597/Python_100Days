import turtle as t 
import random

timmy = t.Turtle()
timmy.shape("turtle")
t.colormode(255)
# timmy.color("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color



color =["red", "blue", "pink", "green", "purple", "orange", "wheat", "IndianRed"]
directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")

for i in range (100):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

# def draw_shape(no_sides):
#     for i in range(no_sides):
#         angle = 360/no_sides
#         timmy.forward(100)
#         timmy.right(angle)

# for i in range(3,11):
#     timmy.color(random.choice(color))
#     draw_shape(i)

# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# for i in range(5):
#     timmy.forward(100)
#     timmy.left(120)


# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)

screen = t.Screen()
screen.exitonclick()
