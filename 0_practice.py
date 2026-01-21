def Frequency(arr, n):
    dic = {}
    for num in arr:
        dic[num] = dic.get(num, 0) + 1

    for num, count in dic.items():
        print(num, count)

arr = [10, 5, 10, 15, 10, 5]
n = len(arr)
Frequency(arr, n)

