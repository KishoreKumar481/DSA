def secondLargest(arr):
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)
    small = float('inf') # +∞
    sec_small = float('inf')
    large = float('-inf') # -∞
    sec_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < sec_small and arr[i] != small:
            sec_small = arr[i]
        if arr[i] > sec_large and arr[i] != large:
            sec_large = arr[i]
    print("Second smallest is", sec_small)
    print("Second largest is", sec_large)

arr = [1, 1, 2, 4, 7, 7, 5]
secondLargest(arr)