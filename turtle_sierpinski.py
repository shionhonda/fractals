# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:51:21 2016 by Shion Honda
"""

import turtle

# Connect the 3 given points
def draw_triangle(tur, point0, point1, point2):
    tur.up()
    tur.goto(point0)
    tur.down()
    tur.goto(point1)
    tur.goto(point2)
    tur.goto(point0)

# Return midpoint between the 2 given points
def midpoint(point0,point1):
    return ((point0[0]+point1[0])/2,(point0[1]+point1[1])/2)
  
# Draw fractal in a recursive way
def sierpinski(tur, point0, point1, point2, level):
    draw_triangle(tur, point0, point1, point2)
    tur.left(120)
    # Recurese if level is positive
    if level > 0:
        sierpinski(tur, point0, midpoint(point0,point1), midpoint(point0,point2),level-1)
        sierpinski(tur, midpoint(point0,point1), point1, midpoint(point1,point2),level-1)
        sierpinski(tur, midpoint(point0,point2), midpoint(point1,point2), point2,level-1)
   
# Execute
wn = turtle.Screen()
ken = turtle.Turtle()
ken.shape('turtle')
point0 = (-100,0)
point1 = (100,0)
point2 = (0,173)
level = 4
sierpinski(ken, point0, point1, point2, level)
ken.hideturtle()
wn.exitonclick()