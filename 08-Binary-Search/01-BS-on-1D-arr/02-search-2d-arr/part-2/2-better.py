def binarySearch(a, target):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == a[mid]:
            return mid
        if target < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def searchMatrix(matrix, target):
    n = len(matrix)

    for i in range(n):
        idx = binarySearch(matrix[i], target)
        if idx != -1:
            return [i, idx]
    return [-1, -1]

matrix = [
            [1,4,7,11,15],
            [2,5,8,12,19],
            [3,6,9,16,22],
            [10,13,14,17,24],
            [18,21,23,26,30]
        ] 
target = 26

print(searchMatrix(matrix, target))
