def getSingleElement(a):
    n = len(a)
    hashmap = {}
    for num in a:
        hashmap[num] = hashmap.get(num, 0) + 1
    for num, count in hashmap.items():
        if count == 1:
            return num
    return -1

a = [1, 1, 2, 3, 3, 4, 4]
ans = getSingleElement(a)
print(f"The single element is {ans}")