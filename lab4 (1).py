import random

even=0
odd=0
for i in range (100):
    r=random.randint(0,100)
    if r%2==0:
        even+=1
    else :
        odd+=1

print("out of 100 random numbers, ",odd,"were odd, and ",even,"were even.")
