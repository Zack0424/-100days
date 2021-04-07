import colorgram
import turtle as t
import random
rgb_colors = []
feri = t.Turtle()

"""
colors = colorgram.extract("image.jpeg", 24)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)"""

colors = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157)]
feri.speed(0)
#TODO: 10x10 size: 20 space: 50
t.colormode(255)
def draw():
    feri.pencolor(random.choice(colors))
    feri.dot(20)


feri.penup()
feri.hideturtle()
for i in range(10):
    feri.setposition(0,i*50)
    for j in range(10):
        feri.setposition(j*50,i*50)
        draw()



screen = t.Screen()
screen.exitonclick()
