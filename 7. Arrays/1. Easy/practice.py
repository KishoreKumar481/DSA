def getLongestSubArray(arr, k):
    n = len(a)
    r, l = 0, 0
    s = a[0]
    ml = 0
    while r < n:
        while l <= r and s > k:
            s -= a[l]
            l += 1

        if s == k:
            ml = max(ml, r - l + 1)

        r += 1
        if r < n:
            s += a[r]
    return ml

a = [1, 2, 3, 1, 1, 1, 1, 3, 3]
k = 6

print(getLongestSubArray(a, k)) # 4