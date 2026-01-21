def inersection(a,b):
    n = len(a)
    m = len(b)
    i, j = 0, 0
    ans = []
    while i < n and j < m:
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            # if len(ans) == 0 or ans[-1] != a[i]: # if you don't want duplicates in the ans (gfg problem)
            ans.append(a[i])
            i += 1
            j += 1
    return ans

a = [1, 2, 2, 3, 3, 4, 5, 6]
b = [2, 3, 3, 5, 6, 6, 7]
print(inersection(a, b)) # [2, 3, 3, 5, 6]