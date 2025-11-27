def getLongestSubArray(arr, k):
    n = len(arr)
    maxLen = 0
    left, right = 0, 0
    sum = arr[0]
    while right < n:
        while left <= right and sum > k:
            left += 1
            sum -= arr[left]
        if sum == k:
            maxLen = max(maxLen, right - left + 1)
        right += 1
        if right < n:
            sum += arr[right]
    return maxLen

a = [1, 2, 3, 1, 1, 1, 1, 3, 3]
k = 6

print(getLongestSubArray(a, k)) # 4