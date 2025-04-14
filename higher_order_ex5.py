import functools

def add(a, b):
    return a + b

l = [2, 4, 5, 6, 7]
print(functools.reduce(add, l, 100))

def myReduce_for(fn, lst, init):
    result = init
    for e in lst:
        result = fn(result, e)
    """
    result = lst[0]
    for e in lst[1:]:
        result = fn(result, e)
    """
    return result

print(myReduce_for(add, l, 100))


def myReduce_rec(fn, lst, init):
    if lst == []:
        return init
    else:
        return fn(lst[0], myReduce_rec(fn, lst[1:], init))


print(myReduce_rec(add, l, 100))
print(myReduce_rec(lambda a, b: a * b, l, 1))