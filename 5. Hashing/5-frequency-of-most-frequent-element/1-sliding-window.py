def maxFrequency(nums, k):
    nums.sort()
    l, r = 0, 0
    res, total = 0, 0
    while r < len(nums):
        total += nums[r]
        while nums[r] * (r - l + 1) > total + k:
            total -= nums[l]
            l += 1
        res = max(res, r - l + 1)
        r += 1
    return res

# nums = [1,2,4]
# k = 5

# nums = [1,4,8,13]
# k = 5

nums = [1, 1, 1, 2, 2, 4]
k = 2

print(maxFrequency(nums, k))