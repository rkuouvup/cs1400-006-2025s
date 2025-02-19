import csv

with open("grade.csv", "r") as f:
    csv_read = csv.reader(f)
    header = next(csv_read)
    grade_book = []
    for row in csv_read:
        #grade_book.append([int(e) for e in row])
        grade_book.append([e.strip() for e in row])

print(header)
print(grade_book)