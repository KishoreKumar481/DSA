def missingNumber(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    s2 = sum(nums)
    return total - s2
    
nums = [3, 0, 1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]

print(missingNumber(nums)) # 2