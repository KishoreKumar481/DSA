def f(i, n):
    if i > n:
        return
    f(i + 1, n)
    print(i)

n = 3
f(1, n)