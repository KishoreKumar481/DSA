def searchMatrix(matrix, tar):
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = n * m - 1

    while low <= high:
        mid = (low + high) // 2
        row = mid // m
        col = mid % m

        if matrix[row][col] == tar:
            return True
        if matrix[row][col] < tar:
            low = mid + 1
        else:
            high = mid - 1

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))
