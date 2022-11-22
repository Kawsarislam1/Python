import math

f = open("data.txt", 'r')
L = []

for line in f:
    line = line.split(" ")
    x = float(line[0])
    y = float(line[1])
    L.append([x,y])

f.close

def distance (p1,p2):
    d = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return d

x = "    {0:6}{1:6}{2:6}{3:6}{4:6}{5:6}{6:6}{7:6}{8:6}".format("P1", "P2","P2","P3", "P4","P5","P6", "P7","P8")
print(x)

dis = []

for i in range (len(L)):
    dis.append([0]*8)


for i in range (len(L)):
    for j in range(len(L)):
        dis[i][j] = distance(L[i],L[j])

for i in range(len(L)):
    print("P{0:<5}{1:<6.2f}{2:<6.2f}{3:<6.2f}{4:<6.2f}{5:<6.2f}{6:<6.2f}{7:<6.2f}{8:6.2f}".
          format(i+1, dis[i][0],dis[i][1],dis[i][2],dis[i][3],dis[i][4],dis[i][5],dis[i][6],dis[i][7]))
