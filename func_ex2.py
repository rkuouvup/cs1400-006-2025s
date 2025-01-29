"""

define function which accept three numbers
print the largest one of the three numbers in the function

"""
def max_three_nums(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            max = n1
        else:
            max = n3
    else:
        if n2 > n3:
            max = n2
        else:
            max = n3
    #print(f"The maximum number of {n1}, {n2}, {n3} is {max}")
    return max

max1 = max_three_nums(8, 3, 2)
max2 = max_three_nums(5, 9, 3)
max3 = max_three_nums(2, 3, 4)
maxmax = max_three_nums(max1, max2, max3)
print(maxmax)