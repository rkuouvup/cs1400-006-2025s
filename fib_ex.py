def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(0))   #0
print(fib(2))   #1
print(fib(4))   #3
print(fib(7))   #13