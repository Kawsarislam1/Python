import random

def three_heads():
    x=[]
    while len(x) <3 or x [-3:] != [0,0,0]:
        y=random.randint(0,1)
        x.append(y)
        if y == 0:
            print('H',end= ' ')
        else:
            print ('T', end= ' ')
    print()
    print("Three heads in a row!")

three_heads()
input()
        
    
