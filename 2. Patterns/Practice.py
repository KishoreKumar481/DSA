def rightTriangle(n):
    for i in range(n):
        start = 65 + n - 1
        for j in range(i + 1):
            print(chr(start - i + j), end=' ')
        print()

n = 5
rightTriangle(n)