def rotateLeft(nums, n , k):
    k %= n
    nums[:] = nums[k:] + nums[:k]
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
n = len(nums)
k = 3
print(rotateLeft(nums, n, k))