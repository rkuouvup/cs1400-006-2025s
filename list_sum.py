l = [5, 4, 7, 2, 9, 8]
#print(sum(l))
"""
5 + 4 => 9
9 + 7 => 16"""

num_sum = 0
"""
num_sum = num_sum + l[0] --> 5
num_sum = num_sum + l[1] --> 9
num_sum = num_sum + l[2] --> 16"""
for i in range(len(l)):
    num_sum = num_sum + l[i]

print(num_sum)