def removeDups(arr):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i + 1] = arr[j]
            i += 1
    print(f'The number of unique elements: {i + 1}')
    print(f'The unique elements: {arr[:i+1]}')

arr = [1, 1, 2, 2, 2, 3, 3]
removeDups(arr)