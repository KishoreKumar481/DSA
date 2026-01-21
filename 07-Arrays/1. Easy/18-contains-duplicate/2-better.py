def containsDuplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
