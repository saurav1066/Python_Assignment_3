"""
Merge Sort
"""


def merge_sort(lis):
    i = 0
    j = 0
    k = 0
    if len(lis) > 1:
        mid_part = len(lis) // 2
        left_part = lis[:mid_part]
        right_part = lis[mid_part:]

        merge_sort(left_part)
        merge_sort(right_part)

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                lis[k] = left_part[i]
                i += 1
            else:
                lis[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            lis[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            lis[k] = right_part[j]
            j += 1
            k += 1
    return lis


result = merge_sort([4, 2, 5, 1, 7, 6, 7])
print(result)