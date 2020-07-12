"""
Bubble Sort
"""

lis = [2, 1, 4, 5, 6, 3, 5, 8]
for i in range(len(lis) - 1):
    for j in range(len(lis) - i - 1):
        if lis[j] > lis[j + 1]:
            lis[j], lis[j + 1] = lis[j + 1], lis[j]
print(lis)
