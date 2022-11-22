print ( "first nested loop")
print("\n")

for row in range (1, 8) :
    for column in range(1, row+1):
        print('*', end = ' ')
    print ()

print("\n")

print ("second nested loop")

print("\n")

for row in range(7, 0, -1):
    for column in range (1, row+1):
        print('*', end= ' ')
    print ()
