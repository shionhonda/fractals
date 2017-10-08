# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 23:54:16 2016 by Shion Honda
"""

import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.image import imread

#定数
c = complex(0, 0.75)
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
    zy = im*(yb-ya)/(imgx-1)+ya
    for re in range(imgy):
        zx = re*(xb-xa)/(imgy-1)+xa
        z = zx+zy*1j
        for i in range(256):
            if abs(z) > 2*max(abs(c),1):
                break
            z = z*z+c
        image.putpixel((re, im), (i%4*64, i%16*16, i%64*4))      
#画像の保存
image.save("julia.png", "PNG")
img = imread("julia.png")
plt.imshow(img)
plt.show()
