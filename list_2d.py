class_grades = [[85, 78, 61],
                [86, 92, 77],
                [78, 78, 87],
                [91, 87, 83]]
std_avg_score = []
for std in class_grades:
    total = 0
    for e in std:
        total = total + e
    grade = total / len(std)
    std_avg_score.append(grade)
print(std_avg_score)