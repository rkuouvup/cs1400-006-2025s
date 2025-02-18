import random
f = open("temp.txt", "r")
"""
for i in range(10):
    line = f.readline()
    print(f"{i+1}: {line}")
"""
line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.seek(random.randint(0, 50))
line = f.readline()
print(line)

f.close()