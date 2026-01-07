def f(i, sum):
    if i < 1:
        print(sum)
        return
    f(i - 1, sum + i)

n = 3
f(n, 0) # o/p: 6