def maxSubArr(a):
    n = len(a)
    maxi = float('-inf')
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j + 1):
                sum += a[k]
            maxi = max(maxi, sum)
    return maxi

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArr(a))
