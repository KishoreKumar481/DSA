def removeDups(arr):
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    j = 0
    for x in st:
        arr[j] = x
        j += 1
    print(f'The number of unique elements: {k}')
    print(f'The unique elements are: {arr[:k]}')

arr = [1, 1, 2, 2, 2, 3, 3]
removeDups(arr)