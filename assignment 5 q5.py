from cImage import*

def dark(old):
    red = (int(old.getRed()/2))*1
    green = (int(old.getGreen()/2))*1
    blue = (int(old.getBlue()/2))*1
    new = Pixel(red, green, blue)
    return new

def turndark (imageFile):
    oldpic = FileImage(imageFile)
    x = oldpic.getWidth()
    y = oldpic.getHeight()

    myImageWindow = ImageWin ("Negative Image", x * 2)
    oldpic.draw(myImageWindow)
    newpic = EmptyImage (x, y)

    for row in range(y):
        for col in range (x):
            old = oldpic.getPixel(col, row)
            new = dark(old)
            newpic.setPixel(col, row, new)


    newpic.setPosition(x + 1, 0)
    newpic.draw(myImageWindow)
    myImageWindow.exitOnClick()

turndark ("pic.gif")

              
