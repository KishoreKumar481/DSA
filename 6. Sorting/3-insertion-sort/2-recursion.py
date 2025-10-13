def insertion_sort(arr, i, n):
    if i == n: # Base case
        return
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
        
    insertion_sort(arr, i + 1, n)

arr = [6, 5, 4, 3, 2, 1]
n = len(arr)
insertion_sort(arr, 0, n)
print(arr)