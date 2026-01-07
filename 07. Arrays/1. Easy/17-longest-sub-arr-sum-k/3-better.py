def getLongestSubarray(a, k):
    preSumMap = {}
    Sum = 0
    maxLen = 0

    for i in range(len(a)):
        # calculate the prefix sum till index i
        Sum += a[i]

        # if the sum = k, update the maxLen
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k
        rem = Sum - k
        
        # calculate the length and update maxLen
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        
        if Sum not in preSumMap:
            preSumMap[Sum] = i
    
    return maxLen

a = [2, 3, 5, 1, 9]
k = 10
print(getLongestSubarray(a, k))