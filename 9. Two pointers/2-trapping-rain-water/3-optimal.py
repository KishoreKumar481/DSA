def trap(height):
    if not height:
        return 0
    
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax: # this ensures we take the min value
            l += 1
            leftMax = max(leftMax, height[l]) # this step before res prevents the -ve values
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r]) # this step before res prevents the -ve values
            res += rightMax - height[r]
    return res

height = [0,2,0,3,1,0,1,3,2,1]
print(trap(height))
