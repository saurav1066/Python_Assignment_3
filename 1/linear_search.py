"""
linear search
"""


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(f'{x} found at index {i}')
            return True
    print("Element Not Found")
    return False


inp = int(input('Enter element you want to search:'))
lis = [4, 2, 5, 1, 7, 6, 7]
result = linear_search(lis,inp)
