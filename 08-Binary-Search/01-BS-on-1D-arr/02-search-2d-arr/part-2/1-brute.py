def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return [i, j]
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
