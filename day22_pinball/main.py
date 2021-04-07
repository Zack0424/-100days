from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

player1_pos = [-370, 0]
player2_pos = [370,0]




screen = Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("black")

ball = Ball()
paddle1 = Paddle(player1_pos)
paddle2 = Paddle(player2_pos)
scoreboard1 = Scoreboard(-150,250)
scoreboard2 = Scoreboard(150,250)

screen.listen()
screen.onkeypress(fun=paddle1.up,key="w")
screen.onkeypress(fun= paddle1.down,key="s")
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor()< -280:
        ball.collision()

    #collision with right paddle
    if ball.distance(paddle2) < 50 and ball.xcor() >340 or ball.distance(paddle1) < 50 and ball.xcor() <-340:
        ball.paddle_collision()

    if ball.xcor()> 400:
        ball.resetpos()
        scoreboard1.won()
    elif ball.xcor() <-400:
        ball.resetpos()
        scoreboard2.won()
screen.mainloop()
