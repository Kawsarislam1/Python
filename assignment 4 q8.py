def print_average():
    total = 0
    numbers= 0
    n = float(input("Type a number: "))
    if n<0:
        print("Average was 0: ")   
    while n > 0:
        if n > 0:
            total = total + 1
            numbers = numbers + n
            average = numbers/total
            n = float(input("Type a number: "))
        if n < 0:
            print("Average was ",average)
        
print_average()
            
