def moveZeros(nums):
    n = len(nums)
    temp = []
    for i in range(n):
        if nums[i] != 0:
            temp.append(nums[i])

    nz = len(temp) # no of non-zero elements

    for i in range(nz):
        nums[i] = temp[i]

    for i in range(nz, n):
        nums[i] = 0
    return nums

nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 2]
print(moveZeros(nums))