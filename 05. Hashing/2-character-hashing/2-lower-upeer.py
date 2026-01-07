s = input()

# precompute
hash = [0] * 256
for char in s:
    hash[ord(char)] += 1

q = int(input())
for _ in range(q):
    c = input()
    # fetch
    print(hash[ord(c)])