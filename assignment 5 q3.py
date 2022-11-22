from cImage import*


def scale (first, num1, num2) :
    width = first.getWidth()
    height = first.getHeight()
    newpic = EmptyImage (width * num1, height * num2)
    for row in range(height):
        for column in range (width):
            oldPixel = first.getPixel(column,row)
            for i in range(0, num1):
                for j in range (num2):
                    newpic.setPixel(num1*column+i,num2*row+j,oldPixel)

    return newpic

def enlargeImage (imageFile) :
    first = FileImage(imageFile)
    x = first.getWidth()
    y= first.getHeight()
    num1 =int(input("Enlarge x by: "))
    num2 =int(input("Enlarge y by: "))

    myWin = ImageWin ("Enlarge",x * num1, y * num2 )
    first.draw(myWin)

    first.draw(myWin)
    
    newImage= scale (first, num1, num2)
    newImage.setPosition(0, first.getHeight () + 1)
    newImage.draw(myWin)
    myWin.exitOnClick()
    
enlargeImage("butterfly.gif")
