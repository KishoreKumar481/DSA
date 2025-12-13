def sort_colors(a):
    cnt0 = cnt1 = cnt2 = 0

    for num in a:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    index = 0

    for _ in range(cnt0):
        a[index] = 0
        index += 1
    for _ in range(cnt1):
        a[index] = 1
        index += 1

    for _ in range(cnt2):
        a[index] = 2
        index += 1
    return a


nums = [1, 0, 2, 1, 0]
print(sort_colors(nums))

