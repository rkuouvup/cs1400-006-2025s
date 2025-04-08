def fact(n):
    result = n
    while n > 1:
        n = n - 1
        result = result * n
    return result

print(fact(4)) # 4 * 3 * 2 * 1 ==> 24
print(fact(5)) # 120