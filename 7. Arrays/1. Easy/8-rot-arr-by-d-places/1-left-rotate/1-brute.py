def rotateArray(arr, d):
    n = len(arr)
    d = d % n
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in range(d, n):
        arr[i - d] = arr[i]
    for i in range(n - d, n):
        arr[i] = temp[i - (n - d)]
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
print(rotateArray(arr, d))