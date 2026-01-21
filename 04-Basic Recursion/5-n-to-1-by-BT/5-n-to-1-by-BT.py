def fun(i, n):
    if i > n:
        return
    fun(i + 1, n)
    print(i)

n = 3
fun(1, n)