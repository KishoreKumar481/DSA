def sortColors(a):
    count0 = count1 = count2 = 0
    for num in a:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1
    
    for i in range(count0):
        a[i] = 0
    for i in range(count0, count0 + count1):
        a[i] = 1
    for i in range(count0 + count1, len(a)):
        a[i] = 2
    return a
    
a = [1, 0, 2, 1, 0]
print(sortColors(a))