list1 =['be', 'be', 'is', 'not', 'or', 'question', 'that', 'the', 'to', 'to']
def remove_duplicates(list1):
    newlist = []
    for i in range(len (list1)):
        if not list1 [i] in newlist:
            newlist.append(list1[i])
        else:
            print('')

    return newlist
print('original list: ',list1)
print('list after removing duplicates:', remove_duplicates(list1))
