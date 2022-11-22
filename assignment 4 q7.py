import random

def dice_sum():
    sum = int(input("desired dice sum: "))
    while True:
        a=random.randint(1,6)
        b=random.randint(1,6)

        print(a, "and", b, "=", a + b)
        if a+b == sum:
            break

dice_sum()
