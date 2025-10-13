def rotateRight(arr, n, k):
    k %= n
    arr[:] = arr[-k:] + arr[:-k]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 3
print(rotateRight(arr, n, k)) # [5, 6, 7, 1, 2, 3, 4]