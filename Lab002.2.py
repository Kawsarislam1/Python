def future_value():
    P =int(input("Present value: "))
    i = float(input("interest rate: "))
    t = float(input("months: "))

    f =P*(1+i)**t
    
    print("The information for your account is: ")
    print("Present value: $",P)
    print("Interest Rate: %",i)
    print("After 18 months, the value of your account would be $", f)
          
future_value()
