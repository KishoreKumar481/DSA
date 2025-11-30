def rotateArray(a, n, d):
    d = d % n
    a = a[d:] + a[:d]
    return a

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 3
print(rotateArray(arr, n, d)) # [4, 5, 6, 7, 1, 2, 3]