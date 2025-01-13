"""
Please write a program to conver a C to F
Please read C degree from user
The formula is F = C * 9 / 5 + 32
"""
'''
    This is also multiline comment
'''
"""
a = 1
a = a + 1
    1 + 1
a = 2
"""
#c_degree = input("Enter the temperature in C: ")
#c_degree = float(c_degree)
c_degree = float(input("Enter the temperature in C: "))
f_degree = c_degree * 9 / 5 + 32
print("The F degree is " + str(f_degree) + " degree")
# f-string version
print(f"The {c_degree:.2f} F degree is {f_degree} C degree")