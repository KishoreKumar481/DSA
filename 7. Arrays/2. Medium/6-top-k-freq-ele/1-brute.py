def topKFrequent(nums, k):
    n = len(nums)
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    a = []
    for num, cnt in count.items():
        a.append([cnt, num])
    a.sort()
    
    res = []
    while len(res) < k:
        res.append(a.pop()[1])
    return res

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
