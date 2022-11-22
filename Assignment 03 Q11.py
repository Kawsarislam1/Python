rooms = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}
instructor = {'CS101':'Haynes', 'CS102':'Alvardo', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
times = {'CS101':'8:00 am', 'CS102':'9:00 am', 'CS103':'10:00 am', 'NT110':'11:00 am', 'CM241':'1:00 pm'}
course = input("Enter a course number: ")
if course not in rooms:
    print(course, "is an invalid course number")
else:
    print("The details for course", course, "are: ")
    print("Room: ",rooms[course])
    print("Instructor: ",instructor[course])
    print("Time: ", times[course])


