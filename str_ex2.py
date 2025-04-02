"""
def two_upper_four(w):
    counter = 0
    for l in w[:4]:
        if l.isupper():
            counter +=  1
    if counter >= 2:
        return True
    else:
        return False
"""
def two_upper_four(w):
    isupper_check = []
    for l in w[:4]:
        isupper_check.append(l.isupper())
    if sum(isupper_check) >=2:
        return True
    else:
        return False

def upper_first4(s):
    return sum([l.isupper() for l in s[:4]])

str1 = "Python"
str2 = "PyThon"
str3 = "PythoN"

print(upper_first4(str1))
print(upper_first4(str2))
print(upper_first4(str3))