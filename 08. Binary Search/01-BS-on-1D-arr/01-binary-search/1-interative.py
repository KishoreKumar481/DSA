def binarySearch(a, tar):
    n = len(a)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == tar:
            return mid
        elif tar > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


a = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
print(binarySearch(a, target))
