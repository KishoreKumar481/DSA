def power(x, n):
    m = abs(n) # use absolute value calculation
    ans = 1
    while m > 0:
        if m % 2 == 1: # odd exponent
            ans *= x
            m = m - 1
        else:          # even component
            m = m // 2
            x = x * x

    if n < 0:   # if original exponent was negative
        return 1 / ans
    else:
        return ans

x = 10
n = 2
print(power(x, n)) # 0.25