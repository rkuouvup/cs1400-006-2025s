def is_prime(n):  # n%2, n%3, n%4, ... n%12
    start_num = 2
    result = True
    """
    while start_num < n:
        if n % start_num == 0:
            result = False
        else:
            pass
            #result = True
        print(f"n % {start_num} = {result}")
        start_num = start_num + 1"""
    for start_num in range(2, n // 2):
        if n % start_num == 0:
            result = False
            break
        else:
            pass
            #result = True
    return result


num = int(input("Enter a number: "))

if is_prime(num):
    print(f"num is a prime")
else:
    print(f"num is not a prime")

"""
x = is_prime(num)

if x == True:
    print(f"num is a prime")
else:
    print(f"num is not a prime")"""
"""
x = is_prime(num)
if x:
    print(f"num is a prime")
else:
    print(f"num is not a prime")"""