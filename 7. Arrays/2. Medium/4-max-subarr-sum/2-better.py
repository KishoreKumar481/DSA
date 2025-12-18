def maxSubArr(a):
    n = len(a)
    maxi = float('-inf')
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += a[j]
            maxi = max(maxi, sum)
    return maxi

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArr(a)) # 6
