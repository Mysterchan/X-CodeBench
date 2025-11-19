from collections import deque
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    g = [[] for _ in range(N)]
    deg = [0]*N

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        g[a].append(b)
        g[b].append(a)
        deg[a] += 1
        deg[b] += 1

    if M != N:
        print("No")
        return

    if not all(d == 2 for d in deg):
        print("No")
        return

    seen = [False]*N
    q = deque([0])
    seen[0] = True
    cnt = 1
    while q:
        v = q.popleft()
        for to in g[v]:
            if not seen[to]:
                seen[to] = True
                cnt += 1
                q.append(to)

    print("Yes" if cnt == N else "No")

if __name__ == "__main__":
    main()