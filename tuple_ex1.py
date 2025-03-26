l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# expected output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

r = []
for i in range(len(l)):
    r.append(l[i][0:2] + (100,))

print(r)

r = []
for e in l:
    r.append(e[0:2] + (100,))
print(r)

print([e[0:2] + (100,) for e in l])