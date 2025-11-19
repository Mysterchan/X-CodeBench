import sys
from collections import deque

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    T = int(next(it))
    out_lines = []
    for _ in range(T):
        n = int(next(it))
        st = int(next(it))
        w = [0] + [int(next(it)) for _ in range(n)]
        g = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(next(it))
            v = int(next(it))
            g[u].append(v)
            g[v].append(u)

        depth = [0] * (n + 1)
        q = deque([1])
        depth[1] = 0
        while q:
            v = q.popleft()
            for to in g[v]:
                if to == 1 or depth[to] != 0:
                    continue
                depth[to] = depth[v] + 1
                q.append(to)

        dist_st = [-1] * (n + 1)
        q = deque([st])
        dist_st[st] = 0
        while q:
            v = q.popleft()
            for to in g[v]:
                if dist_st[to] == -1:
                    dist_st[to] = dist_st[v] + 1
                    q.append(to)

        ans = 0
        for v in range(1, n + 1):
            if depth[v] > dist_st[v]:
                if depth[v] > ans:
                    ans = depth[v]
        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
