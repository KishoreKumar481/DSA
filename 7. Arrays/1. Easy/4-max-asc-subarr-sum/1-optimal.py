def maxAscendingSum(nums):
    max_sum = cur_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur_sum += nums[i]
        else:
            cur_sum = nums[i]
        max_sum = max(max_sum, cur_sum)
    return max_sum

# nums = [10,20,30,5,10,50]
# nums = [10,20,30,40,50]
nums = [12,17,15,13,10,11,12]
print(maxAscendingSum(nums))