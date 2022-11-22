import random

listL=[]
for i in range(0,5):
  n = random.randint(0,10)
  listL.append(n)
print("Old list: ",listL)

def swap(listL,element1,element2):
    
    listL[element1],listL[element2] = listL[element2],listL[element1]
    return listL


element1,element2= 1,5

print("New List after swapping first and last elements in Old List ",swap(listL,element1-1,element2-1))

def Reverse(newlist):
    return [ele for ele in reversed(newlist)]

newlist = swap(listL,element1-1,element2-1)

print("After reversing New List Elements ",Reverse(swap(listL,element1-1,element2-1)))
