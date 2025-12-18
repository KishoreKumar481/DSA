def two_sum_exists(a, tar):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == tar:
                return "YES"
    return "NO"

def two_sum_indices(a, tar):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == tar:
                return [i, j]
    return [-1, -1]

arr = [2, 6, 5, 8, 11]
target = 14

print(two_sum_exists(arr, target))
print(two_sum_indices(arr, target))