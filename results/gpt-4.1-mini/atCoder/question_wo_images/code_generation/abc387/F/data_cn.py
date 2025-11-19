import sys
sys.setrecursionlimit(10**7)
MOD = 998244353

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 建立圖，邊 i->A[i]-1 表示 x_i ≤ x_{A_i-1}
# 反向邊用於拓撲排序
graph = [[] for _ in range(N)]
indeg = [0]*N
for i in range(N):
    graph[A[i]-1].append(i)
    indeg[i] += 1

# 拓撲排序
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

# 若無法拓撲排序(有環)，則無解
if len(order) < N:
    print(0)
    exit()

# dp[i][k]: 第 i 個節點的 x_i 最大值為 k 時，有多少種分配方式
# 由於條件是 x_i ≤ x_{A_i}，拓撲排序中，A_i 在 i 之前
# 我們從拓撲排序的尾端開始計算，確保先計算 A_i 的 dp

# 反向拓撲順序，方便從 A_i 到 i 傳遞
rev_order = order[::-1]

# 初始化 dp，dp[i] 是長度 M 的陣列
dp = [None]*N

# 對於沒有子節點的點，x_i 可以是 1..M，dp[i][k] = 1
# 對於有子節點的點，dp[i][k] = ∏_{j ∈ children(i)} sum_{t=1}^k dp[j][t]

# 先建立子節點列表
children = [[] for _ in range(N)]
for i in range(N):
    children[A[i]-1].append(i)

for u in rev_order:
    if not children[u]:
        # 沒有子節點，dp[u][k] = 1 for k=1..M
        dp[u] = [1]*(M+1)
    else:
        # 有子節點，先計算每個子節點的前綴和
        prefix = []
        for c in children[u]:
            pre = [0]*(M+1)
            for k in range(1, M+1):
                pre[k] = (pre[k-1] + dp[c][k]) % MOD
            prefix.append(pre)
        dp_u = [0]*(M+1)
        for k in range(1, M+1):
            val = 1
            for pre in prefix:
                val = (val * pre[k]) % MOD
            dp_u[k] = val
        dp[u] = dp_u

# 根節點是拓撲排序中 indeg=0 的點，可能有多個
# 但題目中每個 i 都有 x_i ≤ x_{A_i}，A_i 可能是自己或其他點
# 根節點是 order[0]，因為拓撲排序是從入度0開始
# 答案是 sum_{k=1}^M dp[root][k]

root = order[0]
ans = sum(dp[root][1:]) % MOD
print(ans)