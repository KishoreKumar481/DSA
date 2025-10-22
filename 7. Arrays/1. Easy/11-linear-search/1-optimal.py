def linear_search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1
    
arr = [6, 7, 8, 4, 1]
# arr = [6, 7, 8, 6, 1]
x = 4
print(linear_search(arr, x))