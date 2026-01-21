from typing import List

def getLongestArr(a: [int], k: int) -> int:
    n = len(a)
    length = 0
    for i in range(n):
        for j in range(i, n):
            sum = 0
            for m in range(i, j + 1):
                sum += a[m]
            if sum == k:
                length = max(length, j - i + 1)
    return length

a = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]
k = 3
print(getLongestArr(a, k))