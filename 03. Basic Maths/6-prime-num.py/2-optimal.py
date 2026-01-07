import math

def checkPrime(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    
    return count == 2

if __name__ == '__main__':
    n = 1483
    isprime = checkPrime(n)
    if isprime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

    