def threeSum(a):
    n = len(a)
    st = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] == 0:
                    triplet = tuple(sorted([a[i], a[j], a[k]]))
                    st.add(triplet)
    return [list(triplet) for triplet in st]

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
