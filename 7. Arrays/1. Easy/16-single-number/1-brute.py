def getSingleElement(a):
    n = len(a)
    for i in range(n):
        num = a[i]
        cnt = 0

        for j in range(n):
            if a[j] == num:
                cnt += 1
        
        if cnt == 1:
            return num
    # The line will never execute if the array contains a single element
    return -1

a = [1, 1, 2, 3, 3, 4, 4]
ans = getSingleElement(a)
print(f"The single element is {ans}") # 2