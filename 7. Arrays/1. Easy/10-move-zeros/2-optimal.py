def moveZeros(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 2]
print(moveZeros(nums))