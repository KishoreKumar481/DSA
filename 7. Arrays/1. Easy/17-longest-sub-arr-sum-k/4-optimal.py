def getLongestSubArray(a, k):
    n = len(a)

    left, right = 0, 0
    sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left until sum becomes less or equal to k
        while left <= right and sum > k:
            sum -= a[left]
            left += 1

        if sum == k:
            maxLen = max(maxLen, right - left + 1)
        
        right += 1
        if right < n:
            sum += a[right]
    return maxLen

a = [1, 2, 3, 1, 1, 1, 1, 3, 3]
k = 6

print(getLongestSubArray(a, k)) # 4