"""
Insertion sort
"""

lis = [2, 1, 4, 5, 8, 3, 5, 6]
for i in range(1, len(lis)):
    temp = lis[i]
    j = i - 1
    while j >= 0 and temp < lis[j]:
        lis[j+1] = lis[j]
        j -= 1
    lis[j+1] = temp
print(lis)
