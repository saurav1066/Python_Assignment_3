"""
Binary Search
"""


def binary_search(arr, x):
    mid = len(arr) // 2
    if mid > 0:
        if x < arr[mid]:
            binary_search(arr[:mid], x)
        elif x > arr[mid]:
            binary_search(arr[mid:], x)
        else:
            print("Element found in list...")
            return x
    else:
        print("Element Not Found")
        return False


inp = int(input("Enter element you want to search:"))
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(lis, inp)
