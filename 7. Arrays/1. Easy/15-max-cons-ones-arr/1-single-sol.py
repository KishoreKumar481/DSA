from typing import List

def maxConsecutiveOnes(nums: List[int]) -> int:
    cnt = 0
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
        else:
            cnt = 0
        maxi = max(maxi, cnt)
    return maxi

nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print(f"The maximum consecutive 1's are {maxConsecutiveOnes(nums)}")