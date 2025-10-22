def count(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10
    return count

n = 15634
print(count(n))