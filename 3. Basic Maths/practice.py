import math

def checkPrime(n):
    count = 0
    sqrtN = int(math.sqrt(n))
    for i in range(1, sqrtN + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    if count == 2:
        return True
    else:
        return False

if __name__ == '__main__':
    n = 1483   #1483 is a prime number.
    # n = 17
    # n = 100
    isprime = checkPrime(n)
    if isprime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")