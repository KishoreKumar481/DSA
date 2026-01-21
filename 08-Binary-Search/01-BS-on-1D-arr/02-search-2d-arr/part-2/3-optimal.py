def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    row, col = 0, m - 1

    while row < n and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        if matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return [-1, -1]

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 26

print(searchMatrix(matrix, target))
