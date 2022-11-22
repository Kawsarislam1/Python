X=int(input("Enter the X coordinate: "))
Y=int(input("Enter the Y coordinate: "))
radius=int(input("enter the Radius :"))
        
def inCircle(X,Y, radius):
    if (X**2 + Y**2)<= (radius**2):
        print("Point (",X,",",Y,")is in the circle radius ", radius)
        return True 
    else:
        print("Point (",X,",",Y,")is not in circle radius ", radius)
        return False

inCircle(X,Y, radius)
