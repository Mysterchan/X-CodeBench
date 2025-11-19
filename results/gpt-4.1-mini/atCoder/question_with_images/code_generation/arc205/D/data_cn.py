import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())
# 總N上限5*10^5，故整體dfs可行

for _ in range(T):
    N = int(input())
    if N == 2:
        input()  # 讀p_2
        print(0)
        continue
    p = list(map(int, input().split()))
    # 建樹
    g = [[] for __ in range(N+1)]
    for i in range(2, N+1):
        g[p[i-2]].append(i)

    # dp[u] = 該子樹中未配對的白色節點數
    # 配對策略：將子節點的未配對節點兩兩配對，剩餘的向上傳遞
    # 最終根節點剩餘的未配對節點數為dp[1]
    # 最大配對數 = (N - dp[1]) // 2

    def dfs(u):
        unmatched = 1  # 自己未配對
        for w in g[u]:
            unmatched += dfs(w)
        # 每兩個未配對節點配成一對，剩餘未配對節點數為 unmatched % 2
        return unmatched % 2

    unmatched_root = dfs(1)
    print((N - unmatched_root) // 2)