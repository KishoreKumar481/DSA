def getSingleElement(a):
    xor = 0
    for num in a:
        xor = xor ^ num
    return xor

a = [1, 1, 2, 3, 3, 4, 4]
ans = getSingleElement(a)
print(f"The single element is {ans}")