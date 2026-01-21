def getSingleElement(a):
    n = len(a)
    maxi = max(a)
    hash = [0] * (maxi + 1)
    for num in a:
        hash[num] += 1
    for num in a:
        if hash[num] == 1:
            return num
    return -1

a = [1, 1, 2, 3, 3, 4, 4]
ans = getSingleElement(a)
print(f"The single element is {ans}")