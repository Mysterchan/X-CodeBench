import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seen = set()
ans = 0
for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        ans += 1
    else:
        if u > v:
            u, v = v, u
        if (u, v) in seen:
            ans += 1
        else:
            seen.add((u, v))
print(ans)