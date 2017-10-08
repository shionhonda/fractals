# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 22:17:35 2016 by Shion Honda
"""

#import numpy as np
import matplotlib.pyplot as plt

#Plotting range
xmin = 0
xmax = 2.0
ymin = 0
ymax = 2.0
plt.figure(figsize=(5,5))
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

def draw(x1,x2,x3,y1,y2,y3):
    x4 = (x1+x2)/2
    x5 = (x2+x3)/2
    x6 = (x3+x1)/2
    y4 = (y1+y2)/2
    y5 = (y2+y3)/2
    y6 = (y3+y1)/2
    plt.plot([x4,x5],[y4,y5],'black')
    plt.plot([x5,x6],[y5,y6],'black')
    plt.plot([x6,x4],[y6,y4],'black')
    if x2-x1>0.1:
        draw(x1,x4,x6,y1,y4,y6)
        draw(x4,x2,x5,y4,y2,y5)
        draw(x6,x5,x3,y6,y5,y3)

x1 = 0
x2 = 2
x3 = (x1+x2)/2
y1 = 0
y2 = 0
y3 = y1+1.73205*(x2-x1)/2
plt.plot([x1,x2],[y1,y2],'black')
plt.plot([x2,x3],[y2,y3],'black')
plt.plot([x3,x1],[y3,y1],'black')
draw(x1,x2,x3,y1,y2,y3)
plt.show()