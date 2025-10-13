def secondSmallest(arr, n):
    if n < 2:
        return -1
    small = float('inf')
    sec_small = float('inf')
    for i in range(n):
        if arr[i] < small:
            sec_small = small
            small = arr[i]
        elif arr[i] < sec_small and arr[i] != small:
            sec_small = arr[i]
    print(f"Second smallest is {sec_small}")

def secondLargest(arr, n):
    if n < 2:
        return -1
    large = float('-inf')
    sec_large = float('-inf')
    for i in range(n):
        if arr[i] > large:
            sec_large = large
            large = arr[i]
        elif arr[i] > sec_large and arr[i] != large:
            sec_large = arr[i]
    print(f"Second largest is {sec_large}")

arr = [1, 1, 2, 4, 7, 7, 5]
n = len(arr)
secondSmallest(arr, n)
secondLargest(arr, n)
