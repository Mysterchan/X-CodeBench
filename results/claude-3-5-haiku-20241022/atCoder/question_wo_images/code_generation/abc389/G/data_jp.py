def solve():
    N, P = map(int, input().split())
    
    max_edges = N * (N - 1) // 2
    
    # dp[m][mask] = m辺使って、頂点1からの距離が奇数の頂点集合がmaskであるグラフの数
    # maskはビットマスクで、頂点1を除く頂点2..Nについて、距離が奇数なら1
    
    # 全ての可能な辺のリスト
    edges = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            edges.append((i, j))
    
    # 動的計画法
    # dp[使った辺の集合] = 到達可能な頂点とその距離のパリティ
    # ただし、全辺を列挙すると指数的になるので、別のアプローチが必要
    
    # より効率的なアプローチ: 各辺数について、条件を満たすグラフを数える
    # BFSで距離パリティを計算し、連結性と条件をチェック
    
    from collections import deque
    
    def check_graph(edge_set):
        # 隣接リスト構築
        adj = [[] for _ in range(N + 1)]
        for e_idx in edge_set:
            u, v = edges[e_idx]
            adj[u].append(v)
            adj[v].append(u)
        
        # BFSで頂点1から各頂点への距離を計算
        dist = [-1] * (N + 1)
        dist[1] = 0
        q = deque([1])
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        
        # 連結性チェック
        if any(dist[i] == -1 for i in range(1, N + 1)):
            return False
        
        # 偶数距離と奇数距離の頂点数をカウント
        even_count = sum(1 for i in range(1, N + 1) if dist[i] % 2 == 0)
        odd_count = sum(1 for i in range(1, N + 1) if dist[i] % 2 == 1)
        
        return even_count == odd_count
    
    results = []
    
    # 各辺数mについて
    for m in range(N - 1, max_edges + 1):
        count = 0
        
        # m辺を選ぶ全ての組み合わせを試す
        from itertools import combinations
        
        for edge_set in combinations(range(len(edges)), m):
            if check_graph(edge_set):
                count += 1
        
        results.append(count % P)
    
    print(' '.join(map(str, results)))

solve()