def print1(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ') # If you set end=' ', Python will put a space instead of a newline.
        print()

def print2(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print()

def print3(n):
    for i in range(1, n + 1): # outer loop (rows)
        for j in range(1, i + 1): # inner loop (print 1 to i)
            print(j, end=' ')
        print()

def print4(n):
    for i in range(1, n + 1): # outer loop (rows)
        for j in range(1, i + 1): # inner loop (print 1 to i)
            print(i, end=' ')
        print()
  
def print5(n):
    for i in range(n, 0, - 1):
        for j in range(i):
            print('*', end= ' ')
        print()

def print6(n):
    for i in range(n, 0, - 1):
        for j in range(1, i + 1):
            print(j, end= ' ')
        print()

def print7(n):
    for i in range(n):
        # Space
        for j in range(n - i - 1):
            print(' ', end='')

        # Star
        for j in range(2*i + 1):
            print('*', end='')

        # Space
        for j in range(n - i - 1):
            print(' ', end='')
        
        print()

def print8(n):
    for i in range(n):
        # Space
        for j in range(i):
            print(' ', end='')

        # Star
        for j in range(2*n - 2*i - 1):
            print('*', end='')
        print()

def print9(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        
        for j in range(2*i + 1):
            print('*', end='')
        print()
    
    for i in range(n):
        for j in range(i):
            print(' ', end='')
        
        for j in range(2*n - 2*i - 1):
            print('*', end='')
        print()

def print10(n):
    for i in range(2*n - 1):
        if i < n:
            stars = i + 1
        else:
            stars = 2*n - 1 - i 
        print('*' * stars)

def print11(n):
    start = 1
    for i in range(n):
        if (i % 2 == 0):
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(start, end=' ')
            start = 1 - start
        print()

def print12(n):
    space = 2 * (n - 1)
    for i in range(1, n + 1):
        # numbers
        for j in range(1, i + 1):
            print(j, end='')
        # spaces
        for j in range(1, space + 1):
            print(' ', end='')
        # numbers
        for j in range(i, 0, -1):
            print(j, end='')
        print()
        space = space - 2

def print13(n):
    num = 1
    for i in range(n):
        for j in range(i + 1):
            print(num, end=' ')
            num += 1
        print()
             
def print14(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end=' ') #chr(65) is 'A'
        print()

def print15(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65 + j), end=' ')
        print()

def print16(n):
    for i in range(n):
        ch = chr(65 + i)
        for j in range(i + 1):
            print(ch, end=' ')
        print()

def print17(n):
    for i in range(n):
        # spaces
        for j in range(n - i - 1):
            print(' ', end='')

        # characters
        ch = 65 # ASCII value of 'A'
        breakpoint = (2*i + 1) // 2 # integer midpoint
        for j in range(2*i + 1):
            print(chr(ch), end='')
            if j < breakpoint:
                ch += 1
            else:
                ch -= 1
        print()
    
def print18(n):
    start = 65 + n - 1 # ASCII of last row's first letter (e.g., 'F' if n=6)
    for i in range(n):
        for j in range(i + 1):
            print(chr(start - i + j), end=' ')
        print()

def print18a(n):
    for i in range(n):
        ch = 65 + n - 1
        for j in range(i + 1):
            print(chr(ch), end=' ')
            ch -= 1
        print()

def print19(n):
    iniS = 0 # Initial Space
    for i in range(n):
        # Stars
        for j in range(1, n - i + 1):
            print('*', end='')
        # Spaces
        for j in range(1, iniS + 1):
            print(' ', end='')
        # Stars
        for j in range(1, n - i + 1):
            print('*', end='')
        iniS += 2
        print()

    iniS = 2*n - 2
    for i in range(n):
        # Stars
        for j in range(i + 1):
            print('*', end='')
        # Spaces
        for j in range(iniS):
            print(' ', end='')
        # Stars
        for j in range(i + 1):
            print('*', end='')
        iniS -= 2
        print()

def print20(n):
    spaces = 2*n - 2
    for i in range(1, 2*n - 1 + 1):
        stars = i
        if i > n:
            stars = 2*n - i
        # Stars
        for j in range(stars):
            print('*', end='')
        # Spaces
        for j in range(spaces):
            print(' ', end='')
        # Stars
        for j in range(stars):
            print('*', end='')
        print()
        if (i < n):
            spaces -= 2
        else:
            spaces += 2

def print21(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def print22(n):
    for i in range(2*n - 1):
        for j in range(2*n - 1):
            top = i
            left = j
            right = (2*n - 2) - j 
            down = (2*n - 2) - i
            print(n - min(min(top, down), min(left, right)), end='')
        print()

n = 3
print22(n)