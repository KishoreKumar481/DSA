s = input()

# precompute
hash = [0] * 26
for char in s:
    hash[ord(char) - ord('a')] += 1

q = int(input())
for _ in range(q):
    c = input()
    # fetch
    print(hash[ord(c) - ord('a')])