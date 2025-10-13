def inersection(a, b):
    n1 = len(a)
    n2 = len(b)
    ans = []
    visited = [0] * n2
    for i in range(n1):
        for j in range(n2):
            if a[i] == b[j] and visited[j] == 0:
                ans.append(a[i])
                visited[j] = 1
                break
            if b[j] > a[i]:
                break
    return ans

a = [1, 2, 2, 3, 3, 4, 5, 6]
b = [2, 3, 3, 5, 6, 6, 7]
print(inersection(a, b))