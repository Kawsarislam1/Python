file1= open("thisFile.txt","r")
file2= open("thatFile.txt","w")
lines = file1.readlines()
count=0

for i in lines:
    count=count + 1
    if count % 2 != 0:
        file2.write(i)

file1.close()
file2.close()
