def check(nums):
    n = len(nums)
    count = 1
    for i in range(1, 2*n): # mimicks nums + nums without additional arr
        if nums[(i - 1) % n] <= nums[i % n]: # % is used to prevent i from go to out of bounds
            count += 1
        else:
            count = 1
        if count == n:
            return True
    return n == 1

nums = [3, 4, 5, 1, 2]
# nums = [2, 1, 3, 4]
print(check(nums))