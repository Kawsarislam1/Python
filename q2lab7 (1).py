s = input("Enter the string: ")
r = int(input("The number of Repetition: "))

def repl(s,r):
    a=s*r
    if (r<= 0):
        print(" ")
    else:
        print(s,"->",a)

repl(s,r)
