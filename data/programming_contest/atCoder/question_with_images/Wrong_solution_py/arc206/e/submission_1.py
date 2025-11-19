def solve():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        U = list(map(int, input().split()))
        D = list(map(int, input().split()))
        L = list(map(int, input().split()))
        R = list(map(int, input().split()))

        ans = 0
        for i in range(N-2):
            ans += min(U[i] + D[i], L[i] + R[i])
        print(ans)