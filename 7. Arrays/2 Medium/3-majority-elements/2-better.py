def majorityElement(a):
    n = len(a)
    dic = {}
    for num in a:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
        if dic[num] > n // 2:
            return num

a = [2, 2, 3, 3, 1, 2, 2]
print(majorityElement(a))
