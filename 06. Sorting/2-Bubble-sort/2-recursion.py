def bubble_sort(arr, n):
    if n == 1: # Base case
        return 
    didSwap = 0
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            didSwap = 1
    
    if didSwap == 0:
        return
    
    bubble_sort(arr, n - 1)

arr = [6, 5, 4, 3, 2, 1]
n = len(arr)
bubble_sort(arr, n)
print(arr)