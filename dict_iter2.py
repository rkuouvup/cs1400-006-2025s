field_name = ["Q1", "Q2", "Q3"]
s1 = [85, 78, 61]
s2 = [86, 92, 77]
# std_grade = [[85, 78, 61], [86, 92, 77]]

# s1_grade = {"Q1": 85, "Q2": 78, "Q3": 61}

s1_grade2 = {}
s2_grade2 = {}
avg = []
for (k, v1, v2) in zip(field_name, s1, s2):
    s1_grade2[k] = v1
    s2_grade2[k] = v2
for (v1, v2) in zip(s1, s2):
    avg.append((v1 + v2) /2)
print(s1_grade2)
print(s2_grade2)
print(avg)


"""
s1_grade1 = dict.fromkeys(field_name, 0)
for i in range(len(field_name)):
    s1_grade1[field_name[i]] = s1[i]

print(s1_grade1)
"""