import sys
input = sys.stdin.readline

N, M = map(int, input().split())
AB = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    d1 = a - 1
    d2 = N - b
    if d1 == d2:
        AB[0] += 1
    elif d1 < d2:
        AB[b + d1] += 1
    else:
        AB[a - d2] += 1

# To count pairs (i,j) with i<j and lines intersecting,
# the original code does a O(N^2) sum which is too slow.
# We can optimize by using prefix sums.

# The number of intersecting pairs is sum over i<j of AB[i]*AB[j]
# = (sum(AB)^2 - sum(AB[i]^2)) // 2

total = sum(AB)
sum_sq = 0
for x in AB:
    sum_sq += x * x

ans = (total * total - sum_sq) // 2
print(ans)