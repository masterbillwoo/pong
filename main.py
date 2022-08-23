# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen, Turtle

from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
#paddd = Padle()
screen.setup(height=600,width= 800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

lpaddle = Paddle(350, 0)
rpaddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(lpaddle.go_up, "Up")
screen.onkey(lpaddle.go_down, "Down")
screen.onkey(rpaddle.go_up, "w")
screen.onkey(rpaddle.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with r_paddle

    if ball.distance(lpaddle) < 50 and ball.xcor() > 320 or ball.distance(rpaddle) < 50 and ball.xcor() < -320:
        print("collision")
        ball.bounce_x()

    #detect point winner
    if ball.xcor() > 400:
        print("left win")
        scoreboard.l_point()
        ball.move_speed = 0.1
        ball.reset_position()

    if ball.xcor() < -400:
        print("right win")
        scoreboard.r_point()
        ball.move_speed = 0.1
        ball.reset_position()

screen.exitonclick()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
