def two_sum_exists(a, tar):
    dic = {}
    for i, num in enumerate(a):
        complement = tar - num
        if complement in dic:
            return "YES"
        dic[num] = i
    return "NO"

def two_sum_indices(a, tar):
    dic = {}
    for i, num in enumerate(a):
        complement = tar - num
        if complement in dic:
            return [dic[complement], i]
        dic[num] = i
    return [-1, -1]

a = [2, 6, 5, 8, 11]
target = 14

print(two_sum_exists(a, target)) # YES
print(two_sum_indices(a, target)) # [1, 3]
