import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Group sizes by color
buk = [[] for _ in range(n + 1)]
for i in range(n):
    buk[B[i]].append(A[i])

dlt = sum(B)
ans = 0

# For each color, find length of LIS of sizes (which are distinct)
# Use O(M log M) LIS algorithm per color, total O(N log N)
import bisect

for i in range(n + 1):
    if buk[i]:
        seq = buk[i]
        lis = []
        for x in seq:
            pos = bisect.bisect_left(lis, x)
            if pos == len(lis):
                lis.append(x)
            else:
                lis[pos] = x
        ans += i * len(lis)

print(dlt - ans)