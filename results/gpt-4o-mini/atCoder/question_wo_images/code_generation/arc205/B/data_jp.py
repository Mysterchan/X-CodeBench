def max_black_edges(N, M, edges):
    # 全ての辺の本数
    total_edges = N * (N - 1) // 2
    
    # 黒い辺の本数
    black_edges = M
    
    # 白い辺の本数
    white_edges = total_edges - black_edges
    
    # 操作によって変化する黒い辺の本数
    # 3つの頂点を選ぶことで、最大で3本の白い辺を黒にできる
    # ただし、選んだ3つの頂点の間に既に黒い辺がある場合はその分減る
    # 3つの頂点の組み合わせの数
    max_possible_black_edges = black_edges + (N - 2) * (N - 1) // 2
    
    return max_possible_black_edges

import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:M + 1]]

result = max_black_edges(N, M, edges)
print(result)