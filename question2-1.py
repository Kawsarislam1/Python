
items = {}


def menu():
    menu = """Menu
 --------------------------------------
 1. Look up an email address 
 2. Add a new name and email address
 3. Change an existing email address 
 4. Delete a name and email address
 5. Quit the program
 
    """
    print(menu)


def load_data():
    with open('mails.txt', 'r+') as f:
        nmails = f.readlines()
        if len(nmails) > 0:
            for i in nmails:
                values = i.strip().split(":")
                items[values[0]] = values[1]
    return items



items = load_data()


def look_email(name):
    if name.lower() in items:
        result = "Name:{} \nEmail: {}".format(name, items[name])
        print(result)
    else:
        print('The Specified name was not found')
    return ""


def add_name_mail(name, email):
    if name.lower() in items:
        print('That name already exists')
    else:
        items[name.lower()] = email
        print("Name and addresses have been added")
    return ""


def change_email(name, email):
    if name.lower() not in items:
        print("The specified name was not found")
    else:
        items[name.lower()] = email
        print('Information updated')
    return ""


def delete_name_address(name):
    if name.lower() not in items:
        print("The specified name was not found")
    else:
        del(items[name.lower()])
        print('Information deleted')
    return ""


def save_email():
    with open('mails.txt', 'w+') as f:
        for k, v in items.items():
            f.write("{}:{}\n".format(k.lower(), v))


def main():
    menu()
    print('Enter your choice: ', end='')
    inp = int(input())
    isrun = True

    while isrun:
        if inp == 1:
            print('Enter a name: ', end='')
            name = input()
            print(look_email(name))
        elif inp == 2:
            print('Enter a name: ', end='')
            name = input()
            print('Enter a email: ', end='')
            email = input()
            print(add_name_mail(name, email))
        elif inp == 3:
            print('Enter a name: ', end='')
            name = input()
            print('Enter the new  address: ', end='')
            email = input()
            print(change_email(name, email))

        elif inp == 4:
            print('Enter a name: ', end='')
            name = input()
            print(delete_name_address(name))

        elif inp == 5:
            save_email()
            return

        print('\n')
        menu()
        print('Enter your choice: ', end='')
        inp = int(input())



main()
