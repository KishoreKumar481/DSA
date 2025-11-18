def quickSort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quickSort(a, low, p - 1)
        quickSort(a, p + 1, high)

def partition(a, low, high):
    pivot = a[low]
    i = low
    j = high
    while i < j:
        while a[i] <= pivot and i < high:
            i += 1
        while a[j] > pivot and j > low:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[low], a[j] = a[j], a[low]
    return j

a = [4, 6, 2, 5, 7, 9, 1, 3]
print(f"Unsorted array: {a}")
quickSort(a, 0, len(a) - 1)
print(f"Sorted array: {a}")