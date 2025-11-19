import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    t = int(input())
    # Pre-allocate arrays to avoid repeated allocations
    max_n = 7 * 10**4
    E = [[] for _ in range(max_n + 1)]
    G = [[] for _ in range(2 * max_n + 1)]
    dp = [0] * (max_n + 1)
    ans = [-1] * (max_n + 1)
    siz = [0] * (2 * max_n + 1)
    cnt = [0] * (2 * max_n + 1)
    parent = [0] * (2 * max_n + 1)
    weight = [0] * (2 * max_n + 1)
    dis = [0] * (2 * max_n + 1)

    for _ in range(t):
        n = int(input())
        s = ' ' + input().strip()

        # Clear adjacency lists
        for i in range(1, n + 1):
            E[i].clear()
        # Read tree edges
        for _ in range(n - 1):
            u, v = map(int, input().split())
            E[u].append(v)
            E[v].append(u)

        # Build G with auxiliary nodes to make it a binary tree
        m = n
        for i in range(1, m + 1):
            G[i].clear()
        # We'll process E to build G as a binary tree with auxiliary nodes
        # Use iterative DFS to avoid recursion overhead
        stack = [(1, 0)]
        # We'll remove parent from adjacency to avoid revisiting
        # Copy E to local lists to allow modification
        for i in range(1, n + 1):
            E[i] = E[i][:]

        while stack:
            u, f = stack.pop()
            if f in E[u]:
                E[u].remove(f)

            # While degree > 2, add auxiliary nodes
            while len(E[u]) > 2:
                a = E[u].pop()
                b = E[u].pop()
                m += 1
                G[m].clear()
                # Connect auxiliary node m with a and b
                G[m].append((a, 1 if a <= n else 0))
                G[a].append((m, 1 if a <= n else 0))
                G[m].append((b, 1))
                G[b].append((m, 1))
                E[u].append(m)

            # Connect u with its neighbors
            for v in E[u]:
                G[u].append((v, 1 if v <= n else 0))
                G[v].append((u, 1 if v <= n else 0))

            for v in E[u]:
                stack.append((v, u))

        # Initialize dp and ans arrays
        for i in range(1, n + 1):
            if s[i] == '1':
                dp[i] = 2 * n  # large initial value
                ans[i] = 0
            else:
                dp[i] = 0
                ans[i] = -1
        for i in range(n + 1, m + 1):
            dp[i] = 0
            ans[i] = -1

        W_list = []
        lis1 = []
        lis2 = []
        C = 0

        # Centroid decomposition
        def solve(u, total):
            nonlocal C
            if total == 1:
                return

            # Compute siz and cnt arrays with iterative DFS
            stack = [(u, 0, 0)]  # node, parent, state
            order = []
            while stack:
                node, p, state = stack.pop()
                if state == 0:
                    siz[node] = 1
                    cnt[node] = 1 if node <= n and s[node] == '1' else 0
                    parent[node] = p
                    weight[node] = 0
                    stack.append((node, p, 1))
                    for v, w_ in G[node]:
                        if v != p and cnt[v] == 0:
                            stack.append((v, node, 0))
                else:
                    for v, _ in G[node]:
                        if v != parent[node]:
                            siz[node] += siz[v]
                            cnt[node] += cnt[v]
                    order.append(node)

            # Find centroid edge
            min_max = total + 1
            a = b = w = 0
            stack = [(u, 0)]
            while stack:
                node, p = stack.pop()
                max_part = max(siz[node], total - siz[node])
                if max_part < min_max:
                    min_max = max_part
                    a = node
                    b = p
                    w = weight[node]
                for v, _ in G[node]:
                    if v != p:
                        stack.append((v, node))

            # Remove edge a-b
            # Remove from G[a]
            ga = G[a]
            for i in range(len(ga)):
                if ga[i][0] == b:
                    ga.pop(i)
                    break
            # Remove from G[b]
            gb = G[b]
            for i in range(len(gb)):
                if gb[i][0] == a:
                    gb.pop(i)
                    break

            if cnt[a] > 0 and cnt[u] - cnt[a] > 0:
                # BFS from a
                temp1 = []
                dis[a] = 0
                stack2 = [(a, 0)]
                idx = 0
                while idx < len(stack2):
                    node, p = stack2[idx]
                    idx += 1
                    if node <= n and s[node] == '1':
                        temp1.append((node, dis[node]))
                    for v, w_ in G[node]:
                        if v != p:
                            dis[v] = dis[node] + w_
                            stack2.append((v, node))

                # BFS from b
                temp2 = []
                dis[b] = 0
                stack2 = [(b, 0)]
                idx = 0
                while idx < len(stack2):
                    node, p = stack2[idx]
                    idx += 1
                    if node <= n and s[node] == '1':
                        temp2.append((node, dis[node]))
                    for v, w_ in G[node]:
                        if v != p:
                            dis[v] = dis[node] + w_
                            stack2.append((v, node))

                W_list.append(w)
                lis1.append(temp1)
                lis2.append(temp2)
                C += 1

            if cnt[u] - cnt[a] > 1:
                solve(b, total - siz[a])
            if cnt[a] > 1:
                solve(a, siz[a])

            # Restore edge
            G[a].append((b, w))
            G[b].append((a, w))

        solve(1, m)

        res = [0] * (m + 1)

        # The maximum depth of doubling edges is at most ~18 (2^18 > 2*10^5)
        for d in range(1, 19):
            has_update = False
            for i in range(1, n + 1):
                if dp[i] > 0:
                    ans[i] = d
                    has_update = True
            if not has_update:
                break

            for i in range(C):
                w = W_list[i]
                A = lis1[i]
                B = lis2[i]

                if not A or not B:
                    continue

                maxd1 = max(d_ for _, d_ in A)
                maxd2 = max(d_ for _, d_ in B)

                s1 = [-10**9] * (maxd1 + 2)
                s2 = [-10**9] * (maxd2 + 2)

                # For A->B
                for u, d_ in A:
                    v = dp[u] >> 1
                    if d_ + w > v:
                        continue
                    idx = v - d_ - w
                    if idx >= 0:
                        if idx > maxd2:
                            idx = maxd2
                        if s2[idx] < d_:
                            s2[idx] = d_

                # For B->A
                for u, d_ in B:
                    v = dp[u] >> 1
                    if d_ + w > v:
                        continue
                    idx = v - d_ - w
                    if idx >= 0:
                        if idx > maxd1:
                            idx = maxd1
                        if s1[idx] < d_:
                            s1[idx] = d_

                # Prefix max from right to left
                for i1 in range(maxd1 - 1, -1, -1):
                    if s1[i1] < s1[i1 + 1]:
                        s1[i1] = s1[i1 + 1]
                for i2 in range(maxd2 - 1, -1, -1):
                    if s2[i2] < s2[i2 + 1]:
                        s2[i2] = s2[i2 + 1]

                # Update res for A
                for u, d_ in A:
                    if d_ <= maxd1:
                        val = s1[d_]
                        if val > -10**9:
                            cand = val + d_ + w
                            if cand > res[u]:
                                res[u] = cand

                # Update res for B
                for u, d_ in B:
                    if d_ <= maxd2:
                        val = s2[d_]
                        if val > -10**9:
                            cand = val + d_ + w
                            if cand > res[u]:
                                res[u] = cand

            for i in range(1, n + 1):
                dp[i] = res[i]
                res[i] = 0

        print(' '.join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()