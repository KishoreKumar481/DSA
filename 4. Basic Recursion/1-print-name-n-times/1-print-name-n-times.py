def fun(i, n):
    # Base condition
    if i > n:
        return
    print('Raj')

    # Recursive call
    fun(i + 1, n)

if __name__ == "__main__":
    n = 3
    fun(1, n)