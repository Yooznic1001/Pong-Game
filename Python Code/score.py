from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = -1
        self.score_2 = -1


    def score_1_table(self):
        self.clear()
        self.penup()
        self.score_1 += 1
        self.color("white")
        self.hideturtle()
        self.goto(-50, 250)
        self.write(f"{self.score_1}", align="center", font=("Arial", 20, "normal"))





    def score_2_table(self):
        self.clear()
        self.penup()
        self.score_2 += 1
        self.color("white")
        self.hideturtle()
        self.goto(50, 250)
        self.write(f"{self.score_2}", align="center", font=("Arial", 20, "normal"))

    def side(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.pensize(3)
        self.setheading(90)
        self.goto(x=0, y=-300)
        self.pendown()
        for _ in range (30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()


    def writee(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.write(f"GAME OVER", align="center", font=("Arial", 30, "normal"))



