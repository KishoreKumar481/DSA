def countFreq(arr, n):
    f = {}
    for i in arr:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    
    max_f = 0
    min_f = len(arr)
    max_e = None
    min_e = None

    for ele, count in f.items():
        if count > max_f:
            max_f = count
            max_e = ele
        elif count < min_f:
            min_f = count
            min_e = ele
    
    print(f"Max {max_e}, Min {min_e}")

arr = [10, 5, 10, 15, 10, 5]
n = len(arr)
countFreq(arr, n)