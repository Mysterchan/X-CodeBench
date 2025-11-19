from collections import deque

def solve(n, m, x, y, u, v):
    x = x - 1
    y = y - 1
    u = [_-1 for _ in u]
    v = [_-1 for _ in v]
    has_goal = [False] * n
    G = [[] for i in range(n)]
    for i, j in zip(u, v):
        G[i].append(j)
        G[j].append(i)
        if j == y:
            has_goal[i] = True
        if i == y:
            has_goal[j] = True

    G = [deque(sorted(G[i])) for i in range(n)]

    used = [False] * n
    used[x] = True
    ans = [x]
    while True:
        if x == y:
            break
        nx = x
        while used[nx]:
            if len(G[x]) == 0:
                for j in reversed(range(len(ans))):
                    if has_goal[ans[j]]:
                        ans = ans[:j+1] + [y]
                        return " ".join(map(str, [x+1 for x in ans]))
            else:
                nx = G[x].popleft()
        used[nx] = True
        ans.append(nx)
        x = nx

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, x, y = map(int, input().split())
        u, v = zip(*[map(int, input().split()) for i in range(m)])
        print(solve(n, m, x, y, u, v))