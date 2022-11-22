import math

def retangles():
    l1=int(input("Enter the length of the first rentangle: "))
    w1=int(input("Enter the width of the first retangle: "))
    l2=int(input("Enter the lenght of the second retangle: "))
    w2=int(input("Enter the width of the seconf retangle: "))
    a1=l1*w1
    a2=l2*w2
    print("Area A: ",a1)
    print("Area B: ",a2)
    if a1>a2:
        print("Area A is greater than Area B")
    elif a1<a2:
        print("Area B is greater than Area A")
    else:
        print("Area A is equal to Area B")

retangles()
        
 
