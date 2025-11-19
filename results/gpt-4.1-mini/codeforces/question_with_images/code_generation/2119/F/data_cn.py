import sys
import threading
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    T = int(input())
    # 总节点数上限 10^6，预分配空间避免多次申请
    maxn = 10**6 + 10
    adj = [[] for _ in range(maxn)]
    dist = [0]*maxn
    w = [0]*maxn
    dp = [0]*maxn
    visited = [False]*maxn

    for _ in range(T):
        n, st = map(int, input().split())
        ws = list(map(int, input().split()))
        for i in range(1, n+1):
            w[i] = ws[i-1]
            adj[i].clear()
            dist[i] = -1
            dp[i] = 0
            visited[i] = False

        for __ in range(n-1):
            u,v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # BFS from root=1 to get dist[u]
        from collections import deque
        q = deque([1])
        dist[1] = 0
        while q:
            u = q.popleft()
            for nx in adj[u]:
                if dist[nx] == -1:
                    dist[nx] = dist[u] + 1
                    q.append(nx)

        # 计算dp[u]: 从u开始最多能移动多少次
        # 递归定义：
        # dp[u] = max(0, max_{v in adj[u], v!=parent and dist[v]>dist[u]} (dp[v] + 1 + w[v]))
        # 约束：移动到v时刻t+1，t+1 < dist[v]，即 dist[v] > dist[u]
        # 生命值S初始为1，且w[st]=1保证起点安全
        # 递归时传入parent避免回头

        def dfs(u, parent):
            res = 0
            for v in adj[u]:
                if v == parent:
                    continue
                if dist[v] > dist[u]:
                    dfs(v, u)
                    # 只有当dp[v]+1+w[v]>0时才考虑
                    val = dp[v] + 1 + w[v]
                    if val > 0 and w[v] == 1:
                        # w[v] == 1保证移动到v时生命值增加，避免死亡
                        res = max(res, val)
                    elif val > 0 and w[v] == -1:
                        # 负权重顶点也可能有正贡献，但要保证生命值不为0
                        # 这里不做额外判断，dp[v]已经保证安全
                        res = max(res, val)
            dp[u] = res

        # 由于题目保证 w[st] = 1，且起点生命值S=1
        # 先计算dp
        dfs(st, 0)

        # 输出dp[st]
        print(dp[st])

threading.Thread(target=main).start()