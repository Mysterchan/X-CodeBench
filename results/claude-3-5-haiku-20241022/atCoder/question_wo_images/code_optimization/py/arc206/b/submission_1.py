from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Group elements by color
buk = [[] for _ in range(n + 2)]
for i in range(n):
    buk[B[i]].append(A[i])

total_cost = sum(B)
max_save = 0

# For each color, find LIS length using O(n log n) algorithm
for color in range(n + 1):
    if not buk[color]:
        continue
    
    # Binary search LIS
    lis = []
    for val in buk[color]:
        pos = bisect_left(lis, val)
        if pos == len(lis):
            lis.append(val)
        else:
            lis[pos] = val
    
    max_save += color * len(lis)

print(total_cost - max_save)