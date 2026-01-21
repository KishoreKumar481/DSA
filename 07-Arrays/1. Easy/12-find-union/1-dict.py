def find_union(arr1, arr2):
    freq = {}
    union = []

    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
    
    for num in arr2:
        freq[num] = freq.get(num, 0) + 1
    
    for num in freq:
        union.append(num)
    
    return union

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
print(find_union(arr1, arr2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]