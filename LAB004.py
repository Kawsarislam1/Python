import math

def interger():
    for x in range (i,y + 1 ):
        print(x,end = " ")
       
   

def oddNum():
    for x in range (i+2,y,2):
        print(x, end = " ")

def Sumeven():
    acc=0
    for x in range (i,y+1):
        if x % 2 ==0:
            acc = acc + x
    print(acc, end = " ")


    
i = int(input("enter an odd number "))
y = int(input("enter another number "))
print("print all Numbers:")
interger()
print("")
print("print all odd numbers:")
oddNum()
print("")
print("Print sum of the of the even numbers:")
Sumeven()
