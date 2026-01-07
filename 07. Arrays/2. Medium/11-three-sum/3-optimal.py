def threeSum(a):
    n = len(a)
    a.sort()
    ans = []

    for i in range(n):
        if i > 0 and a[i] == a[i - 1]:
            continue
        j, k = i + 1, n - 1
        while j < k:
            total = a[i] + a[j] + a[k]
            if total == 0:
                ans.append([a[i], a[j], a[k]])
                j += 1
                k -= 1
                while j < k and a[j] == a[j - 1]:
                    j += 1
                while j < k and a[k] == a[k + 1]:
                    k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1
    return ans

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # [[-1, 0, 1], [-1, -1, 2]]
