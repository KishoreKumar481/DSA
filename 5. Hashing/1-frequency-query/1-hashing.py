# Read the array directly
arr = list(map( int, input().split() ))

# Precompute frequency (hash array size 13)
hash_arr = [0] * 13
for num in arr:
    hash_arr[num] += 1

# Read number of queries
q = int(input())

# Process each query
for _ in range(q):
    number = int(input())
    print(hash_arr[number])
