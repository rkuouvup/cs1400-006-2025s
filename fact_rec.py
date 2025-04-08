def fact(n):
    """
    if n > 1:
        result = n * fact(n - 1)
    else:
        result = 1
    """
    if n <= 1:  # base case
        result = 1
    else:
        result = n * fact(n - 1)
    return result

print(fact(4))
print(fact(5))