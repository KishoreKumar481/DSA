import math

def min_eating_speed(piles, h):
    l, r = 1, max(piles)
    while l <= r:
        k = (l + r) // 2
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / k)
        if total_time <= h:
            r = k - 1
        else:
            l = k + 1
    return l

piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h)) 
