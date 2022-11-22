
d=int(input("Enter the number of days: "))
def money(d):
    print()
    print("Days            Pennies")
    print("-------------------------------------")
    p=0.01
    for i in range (1,d+1):
        p=p*2
        print(i, "        ",p)
    t=p-0.01
    print("The total salary for", d, "day is $",t)
    
money(d)
