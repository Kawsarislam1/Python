file = open ('books.txt','r')
list1 = file.readlines()

dict1={}

for books in list1:
    books = books.strip()
    book, author = books.split(',')
    if author in dict1:
        dict1[author] =[dict1[author],book]
    else:
        dict1[author]=[book]

for books in dict1.keys():
    print('{},{}'.format(books,dict1[books]))
          



             

        
