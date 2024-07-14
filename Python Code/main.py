import turtle
from turtle import Screen
from pong import Pong
import time
from ball import Ball
from score import Score
import random
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)
screen.listen()

num = [45, 125, 225, 315]

r_pad = Pong((350, 0))
l_pad = Pong((-350, 0))

score1 = Score()
score2 = Score()
score1.score_1_table()
score2.score_2_table()
side = Score()
side.side()
sidee = Score()

ball = Ball()

ball.setheading(random.choice(num))

screen.onkey(l_pad.go_up, "Up")
screen.onkey(l_pad.go_down, "Down")
screen.onkey(r_pad.go_up, "w")
screen.onkey(r_pad.go_down, "s")
game = True
while game:
    screen.update()

    time.sleep(0.048)
    ball.move()
    ball.check()

    if ball.xcor() > 400 or ball.xcor() < -400:
        sidee.writee()
        game = False



    if ball.distance(l_pad) < 50 and ball.xcor() < -338:
        ball.setheading(ball.heading() * round(random.uniform(1, 2), 2))
        score1.score_1_table()

    if ball.distance(r_pad) < 50 and ball.xcor() > 338:
        ball.setheading(ball.heading() * round(random.uniform(1, 2), 2))
        score2.score_2_table()

screen.exitonclick()

