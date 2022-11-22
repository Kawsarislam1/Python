
print("part a")
list = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for row in range(len(list)):
    for column in range(len(list[row])):
        print(list[row][column],end=" ")
    print()

print ("\n")

print("part b")
for i in range(len(list[0])):
    list[0][i]=1
    
for row in range(1,len(list)):
    for column in range(len(list[0])):
        list[row][column]=3
        
for row in range(len(list)):
    for column in range(len(list[row])):
        print(list[row][column],end=" ")
    print()

print ("\n")

print("part c")
for row in range (len(list)):
    list[row][0] = 2
    
for column in range(1,len(list[0])):
    for row in range(len(list)):
        list[row][column]=list[row][column-1] * 2
        
for row in range(len(list)):
    for column in range(len(list[row])):
        print(list[row][column],end=" ")
    print()
