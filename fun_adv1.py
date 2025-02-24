def foo(x):
    y = bar(x)
    y = x + y
    return y

def bar(x):
    result = 2 * x
    return result

print(foo(3))


"""   Basic Function Composition
def add(x):
    result = x + 2
    return result

def multiple(x):
    result = x * 2
    return result

t = add(5)
x = multiple(t)

print(x)"""