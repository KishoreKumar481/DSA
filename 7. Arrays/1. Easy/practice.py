def rightRotateArray(a, d):
    n = len(a)
    d = d % n 
    a[:] = a[d:] + a[:d]
    return a

arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
print(rightRotateArray(arr, d)) # [5, 6, 7, 1, 2, 3, 4]
