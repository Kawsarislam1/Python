from cImage import*

def enhanceRed (original) :
    original.setRed(255)
    return original


def turnred (imageFile):
    first = FileImage (imageFile)
    x = first.getHeight()
    y = first.getWidth()
    myImageWindow = ImageWin ( "Enhanced Red", y * 2, x)
    first.draw(myImageWindow)
    newImage = EmptyImage (y, x)
    for row in range (x):
        for column in range (y):
            original = first.getPixel (column, row)
            newPixel = enhanceRed (original)
            newImage. setPixel (column, row , newPixel)      
    newImage. setPosition (y + 1,0)
    newImage. draw (myImageWindow)
    myImageWindow.exitOnClick()

    
turnred ( "butterfly.gif")
