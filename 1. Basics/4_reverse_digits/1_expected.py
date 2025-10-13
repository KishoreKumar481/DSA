def reverseDigits(n):
    rev = 0
    while n != 0:
        r = n % 10
        rev = rev * 10 + r
        n //= 10
    return rev

n = 200
print(reverseDigits(n))