def fun(i, n):
    if i > n:
        return
    print(i)
    fun(i + 1, n)

if __name__ == "__main__":
    n = 3
    fun(1, n)