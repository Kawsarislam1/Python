import math

w= float(input("Enter wall space in square feet: "))
g= float(input("Enter paint price per gallon: "))
p= w/115
p=math.ceil(p)
h=p*8
c= g*p
l= h*20
t=c+l
print("Gallons of paint: ",p)
print("Hours of labor: ", h)
print("Paint charges: $",c)
print("Labor Charges: $",l)
print("Total cost: $",t)
         
