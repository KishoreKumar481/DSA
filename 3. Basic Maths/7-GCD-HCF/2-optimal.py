def find_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a 

    if a == 0:
        return b
    else:
        return a
    
if __name__ == '__main__':
    n1 = 20
    n2 = 15
    gcd = find_gcd(n1, n2)
    print(f"GCD of {n1} and {n2} is {gcd}") # GCD of 20 and 15 is 5