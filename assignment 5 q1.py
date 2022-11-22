from cImage import*
import math

p= Pixel(0,0,255)
im = EmptyImage (640,640)
w = ImageWin ("Circle", 640,640)

for i in range (360):
    x= int(100 * math.cos(math.radians(i)))
    y= int(100 * math.sin(math.radians(i)))

    im.setPixel(x+ 250, y + 250, p )

im.draw(w)
