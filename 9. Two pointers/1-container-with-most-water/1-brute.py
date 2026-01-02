def maxArea(height):
    n = len(height)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[j], height[i])
            res = max(res, area)
    return res

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

