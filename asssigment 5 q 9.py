
def getData():
    x = []
    print("Enter highest temperatures for each month of the year.")
    htemp = []
    
    for i in range(12):
        htemp.append( int(input("Month " + str(i + 1)+":")))


    print("Enter lowest temperatures for each month of the year.")
    ltemp = []

    
    for i in range(12):
        ltemp.append(int(input("Month " + str(i + 1)+":")))

    x.append(htemp)
    x.append(ltemp)

    return x
    
def averageHigh(x):
    return sum(x[0])/12

def averageLow(x):
    return sum(x[1])/ 12

def highTemp(x):
    temp = x[0][0]
    
    for i in range(1, len(x[0])):
        if x[0][i] > temp:
            temp = x[0][i]
    return temp

def lowTemp(x):
    temp = x[1][0]
    
    for i in range(1, len(x[1])):
        if x[1][i] < temp:
            temp = x[1][i]
    return temp
                   

x = getData()

print("List of the highest and lowest temperatures for each month of the year")
for r in range(len(x)):
    for c in range(len(x[0])):
        print(x[r][c],end=" ")
    print()

print ("Average high temperature for the year: ",averageHigh(x))
print ("Average low temperature for the year: ",averageLow(x))
print ("Highest high temperature for the year: ",highTemp(x))
print ("lowest low temperature for the year: ",lowTemp(x))



                   
