def pattern18(n):
    first = 65 + n - 1
    for i in range(n):
        for j in range(i + 1):
            print(chr(first - i + j), end=' ')
        print()
n = 4
pattern18(n)

