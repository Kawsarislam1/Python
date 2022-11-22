import random
file = input("Enter the name of the file to which result should be written: ")
x = int(input("Enter the number of random numbers to be written to the file: "))
new = open(file,'w')
for i in range(x):
    i = random.randint (1, 100)
    new.write(str(i)+ '\n')
new.close()
