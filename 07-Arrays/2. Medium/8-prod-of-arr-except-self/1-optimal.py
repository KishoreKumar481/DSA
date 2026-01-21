def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix = prefix * nums[i]
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] = res[i] * postfix
        postfix = postfix * nums[i]
    return res


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # [24, 12, 8, 6]
