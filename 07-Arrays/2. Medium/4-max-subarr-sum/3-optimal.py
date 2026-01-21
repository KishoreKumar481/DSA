def maxSubArr(a):
    n = len(a)
    sum = 0
    maxi = float('-inf')
    for i in range(n):
        sum += a[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:
            sum = 0
    return maxi

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArr(a)) # 6
