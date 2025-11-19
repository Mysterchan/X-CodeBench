import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

N, M = map(int, sys.stdin.readline().split())
A = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))

# グラフの辺を逆向きに作る
# 条件: x_i ≤ x_{A_i} より、i -> A_i の辺がある
# 逆向きにすると、A_i -> i の辺を作ることで、親から子へ値が伝播する形になる
graph = [[] for _ in range(N)]
indeg = [0]*N
for i in range(N):
    graph[A[i]].append(i)
    indeg[i] += 1

# トポロジカルソートで処理順を決める
from collections import deque
q = deque()
for i in range(N):
    if indeg[i] == 0:
        q.append(i)

order = []
while q:
    u = q.popleft()
    order.append(u)
    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

# dp[u][k]: 頂点uの値がkのときの部分木の組み合わせ数
# kは1~M
# ただし、x_i ≤ x_{A_i} の条件から、親の値kに対して子の値は ≤ k
# よって、親の値kが決まれば、子の値は1~kの範囲で選べる

# dpはメモリ節約のため、1-indexedで扱う
dp = [None]*N

# 葉から計算するため、逆順で処理
for u in reversed(order):
    # 子がいなければ dp[u][k] = 1 (どのkでも1通り)
    if not graph[u]:
        dp[u] = [1]*(M+1)
        continue

    # 子がいる場合
    # dp[u][k] = ∏_{v in children} sum_{j=1}^k dp[v][j]
    # なので、子ごとに累積和を計算しておく
    # dp[v]はすでに計算済み
    dp[u] = [0]*(M+1)
    # 子の累積和を計算
    child_cum = []
    for v in graph[u]:
        cum = [0]*(M+1)
        s = 0
        for x in range(1, M+1):
            s += dp[v][x]
            if s >= MOD:
                s -= MOD
            cum[x] = s
        child_cum.append(cum)

    for k in range(1, M+1):
        val = 1
        for cum in child_cum:
            val = val * cum[k] % MOD
        dp[u][k] = val

# 根はA[i] = iの頂点（自己ループ）を探す
# 問題文より、A_iは1~Nの範囲で自己ループがある頂点が必ず1つ以上あるはず
roots = [i for i in range(N) if A[i] == i]
# 根が複数ある場合はそれぞれ独立しているので掛け合わせる
ans = 1
for r in roots:
    s = 0
    for k in range(1, M+1):
        s += dp[r][k]
    ans = ans * (s % MOD) % MOD

print(ans % MOD)