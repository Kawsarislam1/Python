def vowel():
    x=input("Enter a string ")
    string = x.upper()
    print("Old string: ",string)
    counter=0
    list1 = ("A","E","I","O","U")
    
    for i in string:
        if i in list1:
            counter = counter+1
            sentence = string.replace("O", "*").replace("E","*").replace("A","*").replace("I","*").replace("O","*")
    print("New String: ",sentence)
    print("Number of vowel characters: ",counter)

    
    
vowel()

