def palindrome(x):
    rev = 0
    dup = x
    while x > 0:
        ld = x % 10
        rev = (rev * 10) + ld
        x = x // 10
    if dup == rev:
        return True
    else:
        return False

x = 121
print(palindrome(x))
x = 1211
print(palindrome(x))
x = -121
print(palindrome(x))