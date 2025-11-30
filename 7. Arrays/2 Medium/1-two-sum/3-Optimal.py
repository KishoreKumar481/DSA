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

a = [2, 6, 5, 8, 11]
target = 14

print(two_sum_exists(a, target)) # YES