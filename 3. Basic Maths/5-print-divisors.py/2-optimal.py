import math

def findDivisors(n):
    divisors = []

    sqrtN = int(math.sqrt(n))

    for i in range(1, sqrtN + 1):

        if n % i == 0:
            divisors.append(i)

            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors

if __name__ == "__main__":
    number = 36
    divisors = findDivisors(number)

    print(f"Divisors of {number} are: ", end='')
    for d in divisors:
        print(d, end=' ')
    print()