import turtle as t
import random

feri = t.Turtle()
feri.shape("turtle")
feri.color("grey","coral")
#for _ in range(4):
#    feri.fd(100)
#    feri.right(90)

"""
for _ in range(15):
    feri.fd(10)
    feri.penup()
    feri.fd(10)
    feri.pendown()
"""
"""
for i in range(3,11):
    feri.pensize(4)
    t.colormode(255)
    feri.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for j in range(i):

        feri.fd(100)
        feri.right(360/i)
"""
"""
directions = [0,90,180,270]
feri.speed(0)
t.colormode(255)
for _ in range(200):
    feri.pensize(10)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    feri.pencolor(color)
    feri.setheading(random.choice(directions))
    feri.fd(20)

korok = int(input("Hány kör legyen?"))
feri.pensize(1)
feri.speed(0)
t.colormode(255)
for i in range(korok):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    feri.pencolor(color)
    feri.right(360/korok)
    feri.circle(100)

"""







screen = t.Screen()
screen.exitonclick()