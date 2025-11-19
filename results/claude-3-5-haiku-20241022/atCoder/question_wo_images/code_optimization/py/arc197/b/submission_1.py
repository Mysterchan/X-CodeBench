import bisect

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    ts = 0
    ans = 0
    for i in range(N):
        ts += A[i]
        ave = ts / (i + 1)
        tmp = i + 1 - bisect.bisect_right(A, ave, 0, i + 1)
        ans = max(ans, tmp)
    print(ans)

T = int(input())
for _ in range(T):
    solve()