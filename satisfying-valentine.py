import turtle
import random
import colorsys


def draw_square(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()


def color_range(start, end, n):
    start_rgb = colorsys.rgb_to_hsv(*start)
    end_rgb = colorsys.rgb_to_hsv(*end)
    step = [(end_rgb[i] - start_rgb[i]) / (n-1) for i in range(3)]
    return [colorsys.hsv_to_rgb(*[start_rgb[i] + step[i] * j for i in range(3)]) for j in range(n)]

colors_1 = color_range((.56, 0, 1), (0.56, 0, 0.88), 20)
colors_2 = color_range((0.56, 0, 0.88), (0.6, 0.47, 1), 20)

colors = []
for i in range(20):
    colors += color_range(colors_1[i], colors_2[i], 2)

turtle.speed(0)
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
for i, color in enumerate(colors):
    if i >= 30:
        break
    for j in range(30):
        draw_square(j * 20 - 300, 300 - i * 20, color)

def draw_text(text):
    turtle.shape("turtle")
    turtle.speed(0)
    turtle.shapesize(2, 2)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color((0, .29, .29), (0.85, 0.2, 0.53))
    turtle.begin_fill()
    for i in range(36):
        turtle.right(10)
        turtle.forward(300)
        turtle.right(120)
        turtle.forward(300)
        turtle.right(120)
        turtle.forward(300)
    turtle.end_fill()

    turtle.color((1, .99, .82), (0.64, 0, 0))
    turtle.pensize(3.5)
    turtle.begin_fill()
    turtle.left(225)
    turtle.forward(180)
    turtle.circle(90,
            extent=180)
    turtle.left(270)
    turtle.circle(90,
            extent = 180)
    turtle.forward(180)

    turtle.forward(180)
    turtle.circle(90,
            extent=180)
    turtle.right(90)
    turtle.circle(90,
            extent = 180)
    turtle.forward(180)
    turtle.forward(180)
    turtle.circle(90,
            extent=180)
    turtle.right(90)
    turtle.circle(90,
            extent = 180)

    turtle.forward(180)
    turtle.forward(180)
    turtle.circle(90,
            extent=180)
    turtle.right(90)
    turtle.circle(90,
            extent = 180)
    turtle.forward(180)
    turtle.end_fill()
    turtle.goto(0,0)
    turtle.shapesize(1,1)
    turtle.goto(0, -10)
    turtle.right(45 + 90)
    
    turtle.penup()
    turtle.goto(0, -5)
    turtle.pendown()
    turtle.color((0.5,0.09,0.09),(1, .99, .82))
    turtle.write(text, align="center", font=("Fixedsys", 20, "normal"))

draw_text('''your   custom  text
               ❤️''')
turtle.goto(0,-5)
turtle.done()