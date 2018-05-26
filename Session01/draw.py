from turtle import *

color("blue")
speed(-1)
fillcolor("yellow")

begin_fill()

# draw square:
for i in range(4):
    forward(100)
    left(90)

# draw triangle:
for i in range(3):
    forward(100)
    left(120)

# draw a circle:
circle(100)

#draw many circles:
for i in range(70):
    circle(100)
    left(7)
end_fill()

mainloop()