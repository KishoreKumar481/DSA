def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1): # n - 1 bc last element will be sorted
        min_idx = i
        for j in range(i + 1, n): # i + 1 bc you don't have to comapare i with itself
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [13, 46, 24, 52, 20, 9]
selection_sort(arr)
print(arr)
