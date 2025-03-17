n = int(input("Enter a number: "))

#d = dict()
"""d = {1: 100}
for x in range(1, n+1):
    d[x] = x * x"""
d = {x: x*x for x in range(1, n+1)}
print(d)