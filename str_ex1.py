org_str = "python a exercises practice solution"

split_lst = org_str.split(" ")

updated_lst1 = []
for w in split_lst:
    if len(w) > 1:
        new_str = w[0].upper() + w[1:-1] + w[-1].upper()
    else:
        new_str = w.upper()
    updated_lst1.append(new_str)

updated_str1 = " ".join(updated_lst1)
print(updated_str1)

def first_last_upper(w):
    if len(w) > 1:
        new_str = w[0].upper() + w[1:-1] + w[-1].upper()
    else:
        new_str = w.upper()
    return new_str

updated_lst2 = list(map(first_last_upper, split_lst))
print(" ".join(map(first_last_upper, split_lst)))

updated_map3 = map(lambda w: w[0].upper() + w[1:-1] + w[-1].upper() 
                             if len(w) > 1 else w.upper(), 
                   split_lst)
print(" ".join(updated_map3))