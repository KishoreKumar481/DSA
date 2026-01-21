import math

def min_eating_speed(piles, h):
    for speed in range(1, max(piles) + 1):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / speed)
        if total_time <= h:
            return speed

piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h)) # 4
