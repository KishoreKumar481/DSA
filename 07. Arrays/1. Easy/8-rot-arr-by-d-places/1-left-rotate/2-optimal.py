def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateLeft(arr, n, k):
    k = k % n
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
k = 3
print(rotateLeft(arr, n, k))
