import sys
sys.setrecursionlimit(10**7)

MOD = 998244353

N, M = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

# グラフを隣接リストで保持（多重辺もそのまま保持）
graph = [[] for _ in range(N+1)]
for i, (u, v) in enumerate(edges, 1):
    graph[u].append((v, i))
    graph[v].append((u, i))

# サイクル検出用
visited = [False]*(N+1)
parent = [-1]*(N+1)
edge_to_parent = [-1]*(N+1)

cycles = set()  # 辺番号の集合（frozenset）でサイクルを保持（重複排除）

def dfs(u):
    visited[u] = True
    for v, eid in graph[u]:
        if not visited[v]:
            parent[v] = u
            edge_to_parent[v] = eid
            dfs(v)
        elif v != parent[u] and visited[v]:
            # 後退辺を検出 → サイクルが存在
            # u -> ... -> v のパスを辿ってサイクルの辺集合を得る
            # ただし、vはすでに訪問済みなので、uからvまでのパスを親を辿って取得
            cycle_edges = set()
            cur = u
            cycle_edges.add(eid)
            while cur != v:
                cycle_edges.add(edge_to_parent[cur])
                cur = parent[cur]
            if len(cycle_edges) >= 2:
                cycles.add(frozenset(cycle_edges))

# DFSで全頂点からサイクル検出
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)

# cyclesには基本的なサイクル（単純閉路）が入っている
# しかし、問題は「サイクルの個数」＝単純閉路の個数ではなく、
# 「サイクルの辺集合の部分集合の個数」ではない。
# 問題文の定義は「単純閉路」のみを数える。

# ここで注意：
# 問題文の定義は「単純閉路」の個数を求めること。
# つまり、頂点が重複しない閉路の個数。
# 上記の方法で検出したcyclesは単純閉路の集合。

# しかし、多重辺があるため、同じ頂点列でも異なる辺集合のサイクルが存在する可能性がある。
# 上記の方法は単純閉路の辺集合を検出するが、多重辺の違いを区別できていない可能性がある。

# そこで、以下の方法を採用する：
# - Nが最大20なので、頂点数は小さい。
# - 辺数は多いが、頂点数が小さいため、頂点間の多重辺は多くてもM。
# - 頂点間の多重辺を区別して、単純閉路を全列挙する。

# アプローチ：
# - 頂点数が小さいので、頂点の部分集合を全探索し、そこに含まれる辺で閉路判定を行うのは不可能（2^Nは約10^6で可能だが、辺の組み合わせは膨大）
# - 代わりに、頂点数が小さいので、単純閉路をDFSで全列挙する。
# - 多重辺を区別するため、辺番号を使って管理する。

# 単純閉路の全列挙（辺番号の集合で管理）：
# - 各頂点からDFSで単純閉路を探索
# - 探索中の頂点はスタックに保持し、訪問済み頂点は再訪問しない
# - ただし、スタート頂点に戻ることで単純閉路が完成
# - 辺番号の集合を記録し、重複を避けるためにfrozensetで保存
# - 辺の多重辺も区別される

# 実装上の工夫：
# - N=20なので、深さ20までのDFSは可能
# - 探索の枝刈りとして、スタート頂点より大きい頂点にしか戻らないようにして重複を減らす
# - ただし、これだけでは重複排除は不十分なので、サイクルの辺集合をfrozensetで管理し、重複はセットで排除

# 実装：

cycles = set()

def dfs_cycle(start, current, depth, path_vertices, path_edges, visited_vertices):
    for v, eid in graph[current]:
        if v == start and depth >= 2:
            # サイクル完成
            cycle = frozenset(path_edges + [eid])
            cycles.add(cycle)
        elif v > start and v not in visited_vertices:
            dfs_cycle(start, v, depth+1, path_vertices + [v], path_edges + [eid], visited_vertices | {v})

for s in range(1, N+1):
    dfs_cycle(s, s, 0, [s], [], {s})

print(len(cycles) % MOD)