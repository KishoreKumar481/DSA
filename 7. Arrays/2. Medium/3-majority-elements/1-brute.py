def majorityElement(a):
    n = len(a)
    for i in range(n):
        count = 0
        for j in range(n):
            if a[i] == a[j]:
                count += 1
        if count > n // 2:
            return a[i]


a = [2, 2, 3, 3, 1, 2, 2]
print(majorityElement(a))
