def missingNumber(nums):
    n = len(nums)
    hash = [0] * (n + 1)

    # Storing the frequencies
    for i in range(n):
        hash[nums[i]] += 1
    
    # Checking the frequencies for numbers 0 to n
    for i in range(n + 1):
        if hash[i] == 0:
            return i 

    # The following line will never execute. It is to avoid warnings.
    return -1

nums = [3, 0, 1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums)) # 2
