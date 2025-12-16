def binarySearch(a, low, high, tar):
    if low > high:
        return -1
    mid = (low + high) // 2
    if tar == a[mid]:
        return mid
    elif tar > a[mid]:
        return binarySearch(a, mid + 1, high, tar)
    else:
        return binarySearch(a, low, mid - 1, tar)

a = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
print(binarySearch(a, 0, len(a) - 1, target))
