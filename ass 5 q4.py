from cImage import*



def gray(old):
    intens= old.getRed() +old.getGreen()+old.getBlue()
    avgRGB = intens // 3
    
    if avgRGB >= 150:
        avgRGB = 255
    else:
        avgRGB = 0
    newPixel = Pixel(avgRGB, avgRGB, avgRGB)
    
    return newPixel


def turngray(imageFile):
    oldpic = FileImage(imageFile)
    x = oldpic.getWidth()
    y = oldpic.getHeight()
    myImageWindow = ImageWin("Grayscale", x*2,y)
    oldpic.draw(myImageWindow)
    newpic = EmptyImage(x, y)
    for row in range (y):
        for column in range(x):
            old = oldpic.getPixel(column,row)
            newPixel = gray(old)
            newpic.setPixel(column,row,newPixel)
    newpic.setPosition(x + 1,0)
    newpic.draw(myImageWindow)
    myImageWindow.exitOnClick()

    
turngray("butterfly.gif")
