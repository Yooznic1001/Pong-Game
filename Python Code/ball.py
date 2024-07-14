from turtle import Turtle
from pong import Pong
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.setheading(45)
        self.color("white")
        self.penup()


    def move(self):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 30
        # self.goto(new_x, new_y)

        self.forward(20)

    def check(self):
        if self.ycor() > 280:
            if self.xcor() > 0:
                self.setheading(self.heading() * -1)
                self.forward(20)
            else:
                self.setheading(self.heading() * -1)
                self.forward(20)
        elif self.ycor() < -280:
            if self.xcor() > 0:
                self.setheading(self.heading() * -1)
                self.forward(20)
            else:
                self.setheading(self.heading() * -1)
                self.forward(20)
