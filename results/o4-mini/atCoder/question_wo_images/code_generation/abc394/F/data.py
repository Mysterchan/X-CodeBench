import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N = int(input())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    NEG_INF = -10**18
    # DP1_down[u]: maximum size of subtree rooted at u (in u's subtree)
    # when u connects to its parent and is internal (degree 4: needs 1 edge to parent + 3 children).
    DP1_down = [NEG_INF] * (N+1)
    # best_down[u] = best contribution from u to its parent: max(1, DP1_down[u])
    best_down = [1] * (N+1)

    parent = [0]*(N+1)

    def dfs1(u, p):
        parent[u] = p
        # process children
        for v in adj[u]:
            if v == p: continue
            dfs1(v, u)
        # gather child contributions
        vals = []
        for v in adj[u]:
            if v == p: continue
            # best from child v to u
            vals.append(best_down[v])
        if len(vals) >= 3:
            # pick top 3
            vals.sort(reverse=True)
            DP1_down[u] = 1 + vals[0] + vals[1] + vals[2]
        else:
            DP1_down[u] = NEG_INF
        best_down[u] = max(1, DP1_down[u])

    dfs1(1, 0)

    ans = 0

    def dfs2(u, p, best_up_u):
        # build contributions from all neighbors
        # for each neighbor v: contrib[v] = best from v->u
        neigh = adj[u]
        D = len(neigh)
        arr = []
        # gather array of (contrib, v)
        for v in neigh:
            if v == p:
                arr.append((best_up_u, v))
            else:
                arr.append((best_down[v], v))
        # sort descending by contrib
        arr.sort(key=lambda x: x[0], reverse=True)

        # To compute best[u][v] quickly, build idx map
        idx = {}
        for i, (_, v) in enumerate(arr):
            idx[v] = i

        # if u can be root of alkane-subtree: needs deg(u) >= 4
        if D >= 4:
            # sum of top 4
            s4 = arr[0][0] + arr[1][0] + arr[2][0] + arr[3][0]
            candidate = 1 + s4
            nonlocal ans
            if candidate > ans:
                ans = candidate

        # precompute sum_top3 and sum_top4
        if D >= 3:
            sum3 = arr[0][0] + arr[1][0] + arr[2][0]
        else:
            sum3 = 0
        if D >= 4:
            sum4 = sum3 + arr[3][0]
        else:
            sum4 = 0

        # propagate to children
        for v in neigh:
            if v == p: 
                continue
            # compute best_up for child v: best from u->v
            if D < 4:
                b_up = 1
            else:
                i = idx[v]
                if i >= 3:
                    # v's contrib not in top 3
                    b_up = 1 + sum3
                else:
                    # replace arr[i] in top4 with arr[3]
                    b_up = 1 + (sum4 - arr[i][0])
            dfs2(v, u, b_up)

    dfs2(1, 0, 0)

    if ans <= 0:
        print(-1)
    else:
        print(ans)

if __name__ == "__main__":
    threading.Thread(target=main).start()