numbers = (5, 2, 8, 6, 1)

result1 = []
for e in numbers:
    result1.append(e*10)

print(f"result1: {result1}")

result2 = [e*10 for e in numbers]
print(f"result2: {result2}")

def times10(e):
    return e*10
result3 = map(times10, numbers)
print(f"result3: {result3}")
print(f"list(result3): {list(result3)}")

def myMap(fn, lst):
    r = []
    for e in lst:
        r.append(fn(e))
    return r
result4 = myMap(times10, numbers)
print(f"result4: {result4}")

"""
def times10(e):
    return e*10
result3 = map(times10, numbers)
"""
# lambda (parameters): expressions
result5 = list(map(lambda e: e*10, numbers))
print(f"result5: {result5}")