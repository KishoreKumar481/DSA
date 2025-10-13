def rotateRight(arr, n, k):
    n = len(arr)
    arr[:] = arr[-k:] + arr[:-k]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 3
print(rotateRight(arr, n, k))