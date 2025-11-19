import sys
from collections import deque
from typing import List, Tuple

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    T = int(data[ptr])
    ptr += 1

    for _ in range(T):
        n = int(data[ptr])
        ptr += 1
        m = n
        s = ' ' + data[ptr]
        ptr += 1

        E = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u, v = int(data[ptr]), int(data[ptr+1])
            ptr += 2
            E[u].append(v)
            E[v].append(u)

        G = [[] for _ in range(2*n)]
        stack = [(1, 0)]
        while stack:
            u, f = stack.pop()
            if f in E[u]:
                E[u].remove(f)

            tmp = E[u].copy()
            while len(E[u]) > 2:
                a = E[u].pop()
                b = E[u].pop()
                m += 1
                G[m].append((a, 1 if a <= n else 0))
                G[a].append((m, 1 if a <= n else 0))
                G[m].append((b, 1))
                G[b].append((m, 1))
                E[u].append(m)

            for v in E[u]:
                G[u].append((v, 1 if v <= n else 0))
                G[v].append((u, 1 if v <= n else 0))

            for v in tmp:
                stack.append((v, u))

        dp = [0] * (n + 1)
        ans = [-1] * (n + 1)
        for i in range(1, n+1):
            if s[i] == '1':
                dp[i] = 2 * n
            else:
                dp[i] = 0
                ans[i] = -1

        C = 0
        W_list = []
        lis1 = []
        lis2 = []

        def solve(u: int, total: int):
            nonlocal C
            if total == 1:
                return

            siz = [0] * (m + 1)
            cnt = [0] * (m + 1)
            parent = [0] * (m + 1)
            weight = [0] * (m + 1)

            stack = [(u, 0, 0, 0)]
            while stack:
                node, p, w, state = stack.pop()
                if state == 0:
                    siz[node] = 1
                    cnt[node] = 1 if node <= n and s[node] == '1' else 0
                    parent[node] = p
                    weight[node] = w
                    stack.append((node, p, w, 1))
                    for v, w_ in G[node]:
                        if v != p and cnt[v] == 0:
                            stack.append((v, node, w_, 0))
                else:
                    for v, _ in G[node]:
                        if v != parent[node]:
                            siz[node] += siz[v]
                            cnt[node] += cnt[v]

            min_max = float('inf')
            a, b, w = 0, 0, 0
            stack = [(u, 0)]
            while stack:
                node, p = stack.pop()
                current_max = max(siz[node], total - siz[node])
                if current_max < min_max:
                    min_max = current_max
                    a = node
                    b = p
                    w = weight[node]
                for v, _ in G[node]:
                    if v != p:
                        stack.append((v, node))

            for i, (v, _) in enumerate(G[a]):
                if v == b:
                    G[a].pop(i)
                    break
            for i, (v, _) in enumerate(G[b]):
                if v == a:
                    G[b].pop(i)
                    break

            if cnt[a] > 0 and cnt[u] - cnt[a] > 0:
                nonlocal W_list, lis1, lis2
                W_list.append(w)
                dis = [0] * (m + 1)
                temp1 = []
                stack = [(a, 0)]
                while stack:
                    node, p = stack.pop()
                    if node <= n and s[node] == '1':
                        temp1.append((node, dis[node]))
                    for v, w_ in G[node]:
                        if v != p:
                            dis[v] = dis[node] + w_
                            stack.append((v, node))
                lis1.append(temp1)

                dis = [0] * (m + 1)
                temp2 = []
                stack = [(b, 0)]
                while stack:
                    node, p = stack.pop()
                    if node <= n and s[node] == '1':
                        temp2.append((node, dis[node]))
                    for v, w_ in G[node]:
                        if v != p:
                            dis[v] = dis[node] + w_
                            stack.append((v, node))
                lis2.append(temp2)
                C += 1

            if cnt[u] - cnt[a] > 1:
                solve(b, total - siz[a])
            if cnt[a] > 1:
                solve(a, siz[a])

            G[a].append((b, w))
            G[b].append((a, w))

        solve(1, m)

        res = [0] * (n + 1)
        for d in range(1, 19):
            has_update = False
            for i in range(1, n+1):
                if dp[i] > 0:
                    ans[i] = d
                    has_update = True
            if not has_update:
                break

            for i in range(C):
                w = W_list[i]
                A = lis1[i]
                B = lis2[i]

                maxd1 = max((d for _, d in A), default=0)
                maxd2 = max((d for _, d in B), default=0)

                s1 = [-10**9] * (maxd1 + 1)
                s2 = [-10**9] * (maxd2 + 1)

                for u, d in A:
                    v = dp[u] // 2
                    if d + w > v:
                        continue
                    idx = min(maxd2, v - d - w)
                    if idx >= 0:
                        s2[idx] = max(s2[idx], d)

                for u, d in B:
                    v = dp[u] // 2
                    if d + w > v:
                        continue
                    idx = min(maxd1, v - d - w)
                    if idx >= 0:
                        s1[idx] = max(s1[idx], d)

                for i in range(maxd1-1, -1, -1):
                    s1[i] = max(s1[i], s1[i+1])
                for i in range(maxd2-1, -1, -1):
                    s2[i] = max(s2[i], s2[i+1])

                for u, d in A:
                    if d <= maxd1:
                        res[u] = max(res[u], s1[d] + d + w)
                for u, d in B:
                    if d <= maxd2:
                        res[u] = max(res[u], s2[d] + d + w)

            for i in range(1, n+1):
                dp[i] = res[i]
                res[i] = 0

        print(' '.join(map(str, ans[1:n+1])))

if __name__ == "__main__":
    main()
