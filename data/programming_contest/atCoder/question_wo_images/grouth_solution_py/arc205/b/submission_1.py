import sys
def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ct = [0]*N
for _ in range(M):
    u, v = [~-int(i) for i in input().split()]
    ct[u] += 1
    ct[v] += 1
ans = 0
for i in range(N):
    d = N-1-ct[i]
    ans += ct[i]+d//2*2

print(ans//2)