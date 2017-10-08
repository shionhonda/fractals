# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:24:50 2016 by Shion Honda
"""
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.image import imread

#画像サイズ
imgx = 12384
imgy = 12384
image = Image.new("RGB", (imgx, imgy))
#プロット範囲
xa = -2.0
xb = 2.0
ya = -2.0
yb = 2.0
#プロット
for im in range(imgx):
    cy = im*(yb-ya)/(imgx-1)+ya
    for re in range(imgy):
        cx = re*(xb-xa)/(imgy-1)+xa
        c = cx+cy*1j
        z = 0
        for i in range(256):
            if abs(z) > 2*max(abs(c),1): 
                break
            z = z*z+c
        image.putpixel((re, im), (i%64*4, i%16*16, i%4*64))      
#画像の保存
image.save("mandelbrot.png", "PNG")
img = imread("mandelbrot.png")
plt.imshow(img)
plt.show()
