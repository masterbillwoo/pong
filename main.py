# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen, Turtle

from paddle import Paddle

screen = Screen()
#paddd = Padle()
screen.setup(height=600,width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

lpaddle = Paddle(350, 0)
rpaddle = Paddle(-350, 0)




screen.listen()
screen.onkey(lpaddle.go_up, "Up")
screen.onkey(lpaddle.go_down, "Down")
screen.onkey(rpaddle.go_up, "w")
screen.onkey(rpaddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
