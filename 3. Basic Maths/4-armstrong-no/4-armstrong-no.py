def armstrong_no(x):
    dup = x
    digits = len(str(x))
    sum = 0
    while x > 0:
        lastdigit = x % 10
        sum = sum + (lastdigit ** digits)
        x = x // 10
    if sum == dup:
        print("True")
    else:
        print("False")

x = 371
armstrong_no(x)
x = 134
armstrong_no(x)
x = 1634
armstrong_no(x)
