def majorityElement(a):
    n = len(a)
    count = 0
    el = 0
    for i in range(n):
        if count == 0:
            count = 1
            el = a[i]
        elif el == a[i]:
            count += 1
        else:
            count -= 1

    count1 = 0
    for i in range(n):
        if a[i] == el:
            count1 += 1
    if count1 > n // 2:
        return el
    return -1

a = [2, 2, 3, 3, 1, 2, 2]
print(majorityElement(a))
