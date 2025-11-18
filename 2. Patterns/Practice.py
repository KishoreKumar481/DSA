def rightTriangle(n):
    for i in range(n):
        ch = 65 + n - 1
        for j in range(i + 1):
            print(chr(ch - i + j), end=' ')
        print()

n = 3
rightTriangle(n)