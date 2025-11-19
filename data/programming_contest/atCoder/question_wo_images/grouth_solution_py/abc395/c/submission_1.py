from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

INF = 2 * 10**5
ans = INF
dd = defaultdict(lambda: -1)
for i in range(N):
    if dd[A[i]] != -1:
        ln = i - dd[A[i]] + 1
        ans = min(ans, ln)
        dd[A[i]] = i
    else:
        dd[A[i]] = i

print(ans if ans != INF else -1)