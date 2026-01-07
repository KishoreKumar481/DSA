def insertion_sort(a, i, n):
    if i == n:
        return
    j = i
    while j > 0 and a[j - 1] > a[j]:
        a[j - 1], a[j] = a[j], a[j - 1]
        j -= 1
    insertion_sort(a, i + 1, n)

arr = [6, 5, 4, 3, 2, 1]
n = len(arr)
insertion_sort(arr, 0, n)
print(arr)