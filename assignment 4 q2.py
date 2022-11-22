import math

f=open("tempconv.txt", 'w')
f.write("{0:12s}{1:12s}\n".format("Fahrenheit","Celsius"))

for fahrenheit in range(-10,11):
    celsius = (fahrenheit - 32)*(5/9)
    f.write("{0:<12.2f}{1:2f}\n".format(fahrenheit,celsius))

f.close()
