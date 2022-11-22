import math
import random

def software():
    n = random.randint(1,150)
    if n > 0 and n <10:
        c = 25 * n
        total=c
        print("Number of Packages: ", n)
        print("Discount Amount: 0")
        print("Total Amount: ", total)

    elif n >= 10 and n <= 19:
        c = 25 * n
        rate = 0.20
        a = rate * c
        total = c - a
        print("Number of Packages: ", n)
        print("Discount Amount: ", a)
        print("Total Amount: ", total)
    elif n >= 20 and n <= 49:
        c = 25 * n
        rate = 0.30
        a = rate * c
        total = c - a
        print("Number of Packages: ", n)
        print("Discount Amount: ", a)
        print("Total Amount: ", total)
    elif n >=50 and n <= 99:
        c = 25 * n
        rate = 0.40
        a = rate * c
        total = c - a
        print("Number of Packages: ", n)
        print("Discount Amount: ", a)
        print("Total Amount: ", total)
    else:
        c = 25 * n
        rate = 0.50
        a = rate * c
        total = c - a
        print("Number of Packages: ", n)
        print("Discount Amount: ", a)
        print("Total Amount: ", total)

software()





