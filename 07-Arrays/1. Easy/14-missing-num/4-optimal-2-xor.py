def missingNumber(nums):
    n = len(nums)
    xor1 = 0
    xor2 = 0
    for i in range(n):  # use n - 1 if n is given
        xor2 = xor2 ^ nums[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...n-1]
    # xor1 = xor1 ^ n # XOR up to [1...n] # This is not needed in leet code problem bc n is not given
    return xor1 ^ xor2

nums = [3, 0, 1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))  # 2
