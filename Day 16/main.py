import turtle
from turtle import Turtle,Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
my_screen = Screen()

timmy.color("cyan")
timmy.shapesize(2.5)
print(my_screen.canvheight)
for i in range(0,5):
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)

if timmy.position != (0,0):
    print("Really")
my_screen.exitonclick()