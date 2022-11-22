def game():
    n1 = float(input("Enter a number: "))
    n2=float (input("Enter another number: "))
    r=n1+n2
    print("The sum of the number you entered is ",r)
    play= input("Do you want to do that again? (y/n): ")
    if play == "y":
        game()
    elif play == "n":
        ""
    else:
        print("Error!! answer must be (y/n) only!")
        play= input("Do you want to do that again? (y/n): ")
           
game()
