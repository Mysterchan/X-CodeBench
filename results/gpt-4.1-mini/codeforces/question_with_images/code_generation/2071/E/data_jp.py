import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

def modinv(a, m=MOD):
    # Fermat's little theorem for modular inverse (m is prime)
    return pow(a, m-2, m)

t = int(input())
# 合計nが10^5を超えないことが保証されているので、全体で一度に処理可能

for _ in range(t):
    n = int(input())
    p = [0]*(n+1)
    q = [0]*(n+1)
    inv_q = [0]*(n+1)
    for i in range(1, n+1):
        pi, qi = map(int, input().split())
        p[i] = pi % MOD
        q[i] = qi % MOD
        inv_q[i] = modinv(q[i])
    # 木の隣接リスト
    g = [[] for __ in range(n+1)]
    for __ in range(n-1):
        u,v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 頂点iが倒れない確率
    # P_alive[i] = (q[i] - p[i]) / q[i] mod M
    P_alive = [0]*(n+1)
    for i in range(1, n+1):
        P_alive[i] = (q[i] - p[i]) * inv_q[i] % MOD

    # 葉の期待値を求める
    # 葉の定義: 生きている頂点で、隣接している生きている頂点がちょうど1つ
    # 期待値を直接計算するために、葉になる確率を求める
    # 葉になる条件:
    # - 頂点iが生きている
    # - 隣接頂点のうちちょうど1つが生きている
    #   他の隣接頂点は倒れている

    # 葉になる確率を計算
    # P_leaf[i] = P_alive[i] * sum_{j in adj[i]} (P_alive[j] * product_{k in adj[i], k!=j} (1 - P_alive[k]))
    # ただし、(1 - P_alive[k]) = 倒れる確率 = p_k/q_k mod M

    # まず、各頂点の隣接頂点のP_aliveを取得し、(1 - P_alive)も計算
    # 計算量を抑えるために累積積を使う

    P_leaf = [0]*(n+1)
    for i in range(1, n+1):
        deg = len(g[i])
        if deg == 0:
            # 孤立点（n=1のときなど）は葉にならない（辺がないので葉の定義に合わない）
            P_leaf[i] = 0
            continue
        alive_list = [P_alive[j] for j in g[i]]
        dead_list = [(1 - P_alive[j]) % MOD for j in g[i]]

        # 累積積を使って、j番目以外のdeadの積を計算
        prefix = [1]*(deg+1)
        suffix = [1]*(deg+1)
        for idx in range(deg):
            prefix[idx+1] = prefix[idx]*dead_list[idx] % MOD
        for idx in range(deg-1, -1, -1):
            suffix[idx] = suffix[idx+1]*dead_list[idx] % MOD

        s = 0
        for idx in range(deg):
            # j番目が生きている確率
            pj = alive_list[idx]
            # 他の隣接頂点が倒れている確率の積
            others = prefix[idx]*suffix[idx+1] % MOD
            s += pj*others
        s %= MOD
        P_leaf[i] = P_alive[i]*s % MOD

    # 葉の期待値の和
    # 葉の頂点の期待値の和は sum P_leaf[i]
    # 葉の頂点の期待値の2乗の和は sum P_leaf[i]^2
    # 葉の頂点の期待値のペアの期待値は
    # E[#pairs] = (E[(sum X_i)^2] - E[sum X_i]) / 2
    # = ( (sum P_leaf[i])^2 - sum P_leaf[i]^2 ) / 2

    sum_leaf = 0
    sum_leaf_sq = 0
    for i in range(1, n+1):
        sum_leaf += P_leaf[i]
        sum_leaf_sq += P_leaf[i]*P_leaf[i]
    sum_leaf %= MOD
    sum_leaf_sq %= MOD

    ans = (sum_leaf*sum_leaf - sum_leaf_sq) % MOD
    inv2 = (MOD+1)//2
    ans = ans * inv2 % MOD

    print(ans)