# Read the array directly (space-separated integers on one line)
arr = list(map( int, input().split() ))

# ✅ Precompute frequencies with a normal dict
mp = {}
for num in arr:
    mp[num] = mp.get(num, 0) + 1 # get current count (0 if missing) and increment

# Read queries
q = int(input())
for _ in range(q):
    number = int(input())
    # ✅ Fetch frequency (0 if not found)
    print(mp.get(number, 0))