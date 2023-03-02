# Python-turtle-hearts
  # Valentines day and you got no idea what to gift ? Your gf/bf is already mad ? 
  # I got u! 
  # Copy the code and let it run. Due to its duration time, your lover will not be able to wait anymore.
  # When the background is finished, the real cute stuff will start to create itself. 
  # The psychological illusion of waiting, lets the oponent value the 'price' much more.


  So here some tips for dudes who like to custom or just do not like the original :
  
   There are actually two lines with different values, one is more violet another is more blue 
   Together they create am effect of a beautiful doubled gradient bg
   You can experiment with the colours and change them to your likes 
   You can also change the visual of the gradient and make it more visible --> go to line 30 step =... (n-1)<- change the number (only int numbers fit)

__________________________________________________________________________________________
```
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
    step = [(end_rgb[i] - start_rgb[i]) / (n-1) for i in range(3)] # change the steps of the gradient effect
    return [colorsys.hsv_to_rgb(*[start_rgb[i] + step[i] * j for i in range(3)]) for j in range(n)]
    
colors_1 = color_range((.56, 0, 1), (0.56, 0, 0.88), 20)   # --> change the colours for the gradient 
colors_2 = color_range((0.56, 0, 0.88), (0.6, 0.47, 1), 20) # --> second colours line for the gradient 
colors = []
for i in range(20): # change the quantity of lines 
    colors += color_range(colors_1[i], colors_2[i], 2)

turtle.speed(0) # change the speed (set to the fastest)
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
for i, color in enumerate(colors):
    if i >= 30:
        break
    for j in range(30):
        draw_square(j * 20 - 300, 300 - i * 20, color) 

def draw_text(text):
    turtle.shape("turtle") # change the shape of the cursor
    turtle.speed(0) # change the speed for the figure  
    turtle.shapesize(2, 2) 
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color((0, .29, .29), (0.85, 0.2, 0.53)) # change the colourlines for the figure, first for the contouring, second line filling 
    turtle.begin_fill()
    for i in range(36):
        turtle.right(10)
        turtle.forward(300)
        turtle.right(120)
        turtle.forward(300)
        turtle.right(120)
        turtle.forward(300)
    turtle.end_fill()

    turtle.color((1, .99, .82), (0.64, 0, 0)) # change the colours for the Valintene's hearts 
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
    turtle.color((0.5,0.09,0.09),(1, .99, .82)) # change the text colour 
    turtle.write(text, align="center", font=("Fixedsys", 20, "normal")) # change the text font and size

draw_text('''your   custom  text
               ❤️''') # insert your text, experiment with positioning and so on (sry for that, might be a bit hard :/ )
turtle.goto(0,-5)
turtle.done()
```
________________________________________________________________________________________________________

# congrats, now you can enjoy the smile of your lover, and chill out a year, maybe i will do something simillar for the next valentine's day
# I will also post a version where there is no psychological effects, only fast drawings 
# and in the file 'Sample' you'll be able to see, how it will look
# Thanks for attention 
