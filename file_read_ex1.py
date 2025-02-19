with open("grade.csv", "r") as f:
    header = f.readline()
    lines = f.readlines()
    grade_book = []
    for line in lines:
        grade_book.append([int (e) for e in line.strip().split(',')])
        """
        t1 = line.strip() # t1 = '85,78,61'
        t2 = t1.split(',') # t2 = ['85', '78', '61']
        #t3 = []
        #for e in t3:
        #    t3.append(int(e))
        t3 = [int(e) for e in t2] # t3 = [85, 78, 61]
        grade_book.append(t3)
        """


print(grade_book)