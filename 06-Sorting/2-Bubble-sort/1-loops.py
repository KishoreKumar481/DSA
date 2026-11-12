def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        did_swap = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = 1
        if did_swap == 0:
            break


arr = [6, 5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr)

