def list_sum_for(lst):
    result = 0
    for e in lst:
        result = result + e
    return result

def list_sum_rec(lst):
    #if len(lst) == 0:
    if lst == []:
        return 0
    else:
        return lst[0] + list_sum_rec(lst[1:])

l = [2, 4, 5, 6, 7]
print(list_sum_for(l))
print(list_sum_rec(l))