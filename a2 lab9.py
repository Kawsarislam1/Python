x=input("Enter a string: ")
string=x.lower()
vowel=("a","e","i","o","u")
count=0
count2=0

def countvowels(count):
    for i in string:
        if i in vowel:
            count=count+1
    return count
        

def consonants(count2):
    for i in string:
        if i not in vowel:
            count2=count2+1
    return count2
        


    
print("The string you entered includes ",countvowels(count),"vowels and ",consonants(count2),"consonants")
        
    
