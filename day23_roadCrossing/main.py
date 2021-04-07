import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Calls
player = Player()
cars = []
for _ in range(15):
    car = CarManager()
    cars.append(car)

screen.listen()
screen.onkeypress(player.up, "Up")
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # MOVING CARS
    for i in cars:
        i.move()
    for i in cars:
        if i.xcor() < -320:
            i.re()
    # LEVELING UP

    if player.ycor() > player.finish:
        player.re()
        for i in cars:
            i.level_up()
        score.level_up()

    # DETECTING COLLISION WITH CARS
    for i in cars:
        if player.distance(i.xcor(), i.ycor()) < 20 and player.ycor() - i.ycor() < 20:
            score.game_over()
            game_is_on = False
screen.exitonclick()