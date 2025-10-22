def Frequency(arr, n):
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    
    for i in mp:
        print(i, mp[i])
    # print(mp)

arr = [10, 5, 10, 15, 10, 5]
n = len(arr)
Frequency(arr, n)
