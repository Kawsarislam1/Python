from cImage import *
hori = Pixel(0,255,0)
dia = Pixel(255,0,0)
image = EmptyImage(300,300)
Lab12 = ImageWin("Lab 12",300,300)


for m in range (300) :
    image.setPixel (150,m, hori)
for m in range (150,300) :
    image.setPixel (m,m, dia)
for m in range (300) :
    image.setPixel(m, 150, hori)

image.draw(Lab12)
image. save("Lab12.gif")
Lab12.exitonclick
