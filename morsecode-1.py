
def menu():
    menu = """\nHello, this program allows you to translate text to morse code or translate morse code to text. 
    
Please , select one of the below options: 

***Enter 't' for encoding text
***Enter 'm' for decoding morse code
***Enter 'e' to exit the program. 


    """
    return menu


def load_morse():
    item = {}
    file = open('morse.txt', 'r+')
    for i in file.readlines():
        i = i.strip()
        item[i[0].lower()] = i[9:13].strip()
        item[i[13].lower()] = i[22:26].strip()
        if len(i) > 26:
            item[i[26].lower()] = i[35:].strip()
    file.close()
    return item



items = load_morse()


def convert_normal_morse(text):
    lines = text.split()
    count = 0
    result = ''
    while count < len(lines):
      
        for i in lines[count]:
            result += items[i.lower()] + ' '
        result += '   '
        count += 1
    return result


def convert_morse_normal(text):
    reverse_items = {}
    for k, v in items.items():
        reverse_items[v.strip()] = k
    lines = text.split('   ')
    result = ''
    count = 0
    while count < len(lines):
        for i in lines[count].split():
            result += reverse_items[i].upper()
        result += ' '
        count += 1
    return result


def main():
    print(menu())
    print("My input is: ", end='')
    inp = input()
    isrun = True
    while isrun:
        if inp == 't':
            print('Please enter text to translate:')
            selection = input()
            print(convert_normal_morse(selection))
        elif inp == 'm':
            print('Please enter morse to translate:')
            selection = input()
            print(convert_morse_normal(selection))
        elif inp == 'e':
            break
        else:
            if inp not in ['t', 'm', 'e']:
                print('***invalid option.')
            print('Please enter a valid option: ', end='')
            inp = input()
            continue

        print()
        print(menu())
        print("My input is: ", end='')
        inp = input()
    print("\nThanks for using this program!")


main()
