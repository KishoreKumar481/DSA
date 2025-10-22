def quickSort(arr, low, high):
    if low < high:
        # Partition the array
        p = partition(arr, low, high)

        # Sort the left part
        quickSort(arr, low, p - 1)

        # Sort the right part
        quickSort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[low] # Choosing the first element as pivot
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i] # Swap
        
    arr[low], arr[j] = arr[j], arr[low] # Put pivot in correct place
    return j

arr = [4, 6, 2, 5, 7, 9, 1, 3]
print(f"Unsorted array: {arr}")
quickSort(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")