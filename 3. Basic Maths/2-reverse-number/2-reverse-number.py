def reverse_number(m):
    n = abs(m)
    rev = 0
    while n > 0:
        lastdigit = n % 10
        rev = (rev * 10) + lastdigit
        n = n // 10

    if m < 0:
        print(-rev)
    else:
        print(rev)

m = -7789
reverse_number(m)