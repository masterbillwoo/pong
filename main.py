# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen, Turtle

from paddle import Padle

screen = Screen()
#paddd = Padle()
screen.setup(height=600,width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up, "Up")

screen.onkey(go_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/