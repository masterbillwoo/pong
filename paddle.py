from turtle import Screen, Turtle
UP = 90
DOWN = 270

class Padle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        #self.hideturtle()
        #self.shape("square")
        self.color("white")
        self.shape("square")
        self.shapesize(3, 1)
        self.setx(350)
        self.sety(0)

    def up(self):
        self.sety(self.ycor() + 50)

    def down(self):
        self.sety(self.ycor() - 50)


