import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    p = 0
    for a in A:
        if p != a:
            ans += 1
        p = a
    print(ans)