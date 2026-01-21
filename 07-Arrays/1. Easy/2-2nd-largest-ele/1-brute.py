def secondLargest(arr):
    arr = sorted(set(arr)) # sorts and removes duplicates
    n = len(arr)
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
        return
    small = arr[1]
    large = arr[n-2]
    print("Second smallest is", small)
    print("Second largest is", large)

arr = [1, 2, 1, 4, 7, 7, 5]
secondLargest(arr)