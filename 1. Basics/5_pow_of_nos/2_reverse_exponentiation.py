def reverse_num(n):
    rev = 0
    while n > 0:
        r = n % 10
        rev = rev * 10 + r 
        n //= 10
    return rev

def power(n):
    rev = reverse_num(n) # Reverse of n
    ans = 1
    base = n
    exp = rev
    while exp > 0:
        if exp % 2 == 1: # Odd exponent
            ans *= base
            exp -= 1
        else:
            exp //= 2
            base *= base
    return ans

n = 10
print(power(n)) 