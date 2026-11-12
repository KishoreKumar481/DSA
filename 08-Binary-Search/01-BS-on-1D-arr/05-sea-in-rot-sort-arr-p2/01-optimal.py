def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if target == nums[m]:
            return True
        if nums[l] < nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        elif nums[l] > nums[m]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            l += 1
    return False

nums = [2,5,6,0,0,1,2]
target = 0
print(search(nums, target))
