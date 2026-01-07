def two_sum_exists(a, tar):
    a.sort()
    left, right = 0, len(a) - 1

    while left < right:
        s = a[left] + a[right]
        if s == tar:
            return "YES"
        elif s < tar:
            left += 1
        else:
            right -= 1
    return "NO"

def two_sum_indices(a, tar): # leetcode prob question arr is sorted
    l, r = 0, len(a) - 1
    while l < r:
        curSum = a[l] + a[r]
        if curSum > tar:
            r -= 1
        elif curSum < tar:
            l += 1
        else:
            return [l + 1, r + 1]
    return []

a = [2, 6, 5, 8, 11]
target = 14

print(two_sum_exists(a, target)) # YES

nums = [2,7,11,15]
target = 9
print(two_sum_indices(nums, target)) # [1, 2]
