def min_edges_to_remove(N, M, edges):
    from collections import defaultdict

    # グラフの隣接リストを作成
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # 重複辺の数をカウント
    duplicate_edges = 0
    for u in graph:
        duplicate_edges += len(graph[u]) - 1  # 各頂点の隣接リストのサイズから1を引く

    # 自己ループの数をカウント
    self_loops = sum(1 for u, v in edges if u == v)

    # 取り除く必要がある辺の本数
    return duplicate_edges + self_loops

# 入力の読み込み
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M+1]]

# 結果を出力
print(min_edges_to_remove(N, M, edges))