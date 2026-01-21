def maxSubArr(a):
    n = len(a)
    sum = 0
    maxi = float('-inf')
    for i in range(n):
        if sum == 0:
            start = i
        sum += a[i]
        if sum > maxi:
            maxi = sum
            ansStart = start
            ansEnd = i
        if sum < 0:
            sum = 0
    return a[ansStart:ansEnd + 1]

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArr(a)) # [4, -1, -2, 1, 5]
