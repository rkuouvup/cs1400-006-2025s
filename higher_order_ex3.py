nums1 = [1,2,3,4,5,6,7,8]
nums2 = [2,2,3,1,2,6,7,9]
# expected output: 4

# Solution 1: for statement
count1 = 0
for (v1, v2) in zip(nums1, nums2):
    if (v1 == v2):
        count1 = count1 + 1
print(count1)

# Solution 2: [False, True, True, False, False, True, True, False]
count2_list = []
for (v1, v2) in zip(nums1, nums2):
    count2_list.append(v1 == v2)
    """if (v1 == v2):
        count2_list.append(True)
    else:
        count2_list.append(False)"""
print(count2_list)
count2 = sum(count2_list)
print(count2)

# Solution 3: list comprehension
count3_list = [v1 == v2 for (v1, v2) in zip(nums1, nums2)]
count3 = sum(count2_list)
print(sum([v1 == v2 for (v1, v2) in zip(nums1, nums2)]))

# Solution 4: map() with single parameter function

def same_pair(e):
    return e[0] == e[1]

count4_map = map(same_pair, list(zip(nums1, nums2)))
print(count4_map)
#count4_list = list(count4_map)
count4 = sum(count4_map)
print(count4)

# Solution 4.5: map() with single parameter lambda expression
count45_map = map(lambda e: e[0] == e[1], list(zip(nums1, nums2)))
print(sum(count45_map))

# Solution 5: map() with two parameters function

def same_pair(v1, v2):
    return v1 == v2

count5_map = map(same_pair, nums1, nums2)
print(sum(count5_map))

# Solution 5.5: map() with two parameters lambda expression
count55_map = map(lambda v1, v2: v1 == v2, nums1, nums2)
print(sum(count55_map))

# Solustion 6: use operator module
from operator import eq
count6 = sum(map(eq, nums1, nums2))
print(count6)
