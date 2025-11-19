def solve():
    N, M = map(int, input().split())
    
    edges = set()
    for _ in range(M):
        u, v = map(int, input().split())
        edges.add((min(u, v), max(u, v)))
    
    # 完全グラフの辺の総数
    total_edges = N * (N - 1) // 2
    
    # 各頂点の黒辺の次数を計算
    degree = [0] * (N + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    
    # 奇数次数の頂点数を数える
    odd_count = sum(1 for i in range(1, N + 1) if degree[i] % 2 == 1)
    
    # 最大黒辺数の計算
    # 奇数次数の頂点が偶数個なら現在の黒辺数を保てる
    # 奇数次数の頂点が奇数個なら1本増減させる必要がある
    
    if odd_count % 2 == 0:
        # 偶数個の場合、最大化は total_edges - M と M の大きい方
        max_black = max(M, total_edges - M)
    else:
        # 奇数個の場合、1本変更が必要
        # M から 1 引くか、total_edges - M から 1 引くか
        max_black = max(M - 1, total_edges - M - 1)
    
    print(max_black)

solve()