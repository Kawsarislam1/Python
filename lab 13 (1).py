def twodlist (List) :
    print ("2D List: ")
    for col in List:
        for row in col:
            print (row, end = " ")
        print ()

    print ("Number of odd negative values: ")
    for col in range (len(List)):
        print ("col", col + 1, end = ": ")
        count = 0
        for row in range (len (List[col])) :
            if List[col][row] % 2 != 0 and List[col][row] < 0  :
                count += 1
        print (count)

sample = [-2, 3, -5], [-8, 4, -6], [9, -3, 77], [11,-2, 9]


twodlist (sample)
