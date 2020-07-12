"""
Interpolation Search
pos = lo + [(x - arr[lo]) * (hi - lo) / (arr[hi] - arr[Lo])]
"""


def interpolation_search(arr, x):
    pos = (x - arr[0]) * (len(arr) - 1) // (arr[len(arr)-1] - arr[0])
    if 0 < pos < len(arr):
        if x < arr[pos]:
            interpolation_search(arr[:pos], x)
        elif x > arr[pos]:
            interpolation_search(arr[pos:], x)
        else:
            print("Element found in list...")
            return x
    else:
        print("Element Not Found")
        return False


inp = int(input("Enter element you want to search:"))
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = interpolation_search(lis, inp)
