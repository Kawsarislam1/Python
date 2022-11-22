original = ['how', 'are', 'you?']
def double_list(original):
    newlist = []
    for i in range(len(original)):
        newlist.append(original[i])
        newlist.append(original[i])
    return (newlist)
print('original list: ', original)
print('double list: ', double_list(original))
