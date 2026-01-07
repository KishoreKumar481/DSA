def threeSum(a):
    n = len(a)
    ans = set() # to store unique triplets

    for i in range(n):
        hashset = set() # to store ele stores in this iteration

        for j in range(i + 1, n):
            third = -(a[i] + a[j])

            if third in hashset:
                triplet = tuple(sorted([a[i], a[j], third]))
                ans.add(triplet)

            hashset.add(a[j])

    return [list(triplet) for triplet in ans]


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums)) # [[-1, 0, 1], [-1, -1, 2]]
