def checkPrime(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
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