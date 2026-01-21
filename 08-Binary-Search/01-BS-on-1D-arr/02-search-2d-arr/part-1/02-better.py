def binarySearch(a, tar):
    n = len(a)
    low, high = 0, n - 1
    while low < high:
        mid = (low + high) // 2
        if a[mid] == tar:
            return True
        if tar > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


def searchMatrix(matrix, tar):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][0] <= tar <= matrix[i][m - 1]:
            return binarySearch(matrix[i], target)
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))
