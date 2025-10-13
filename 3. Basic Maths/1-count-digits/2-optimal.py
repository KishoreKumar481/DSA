import math

def countDigits(n):
    count = int(math.log10(n) + 1)
    return count

if __name__ == '__main__':
    N = 329823
    print('n:', N)
    digits = countDigits(N)
    print("Number of digits in N:", digits)