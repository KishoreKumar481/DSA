def maxArea(height):
    n = len(height)
    l, r = 0, n - 1
    res = 0
    while l < r:
        area = (r - l) * min(height[l], height[r]) # taking the smaller height since it is the breaking height
        res = max(res, area)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return res

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
