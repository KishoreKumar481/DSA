def count_dividing_digits(n):
    count = 0
    for digit_char in str(n):
        digit = int(digit_char)
        if digit != 0 and n % digit == 0:
            count += 1
    return count

n = 23
print(count_dividing_digits(n))