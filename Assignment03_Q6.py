import math
a = float(input('Enter Number: '))
b = float(input('Enter Number: '))
c = float(input('Enter Number: '))
d = float(input('Enter Number: '))
e = float(input('Enter Number: '))
f = float(input('Enter Number: '))
g = float(input('Enter Number: '))
h = float(input('Enter Number: '))
i = float(input('Enter Number: '))
j = float(input('Enter Number: '))
my_list = [a, b, c, d, e, f, g, h, i, j]
total = sum (my_list)
low = my_list[0]
high = my_list[9]
for k in range(1,len(my_list)) :
    if my_list[k] < low:
         low = my_list[k]
    elif my_list[k] > high:
         high = my_list[k]
average = sum(my_list) / 10
print("Low: ",low,'\n',"High: ",high,'\n',"Total: ",total,'\n', "Average:",average)

