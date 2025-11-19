import sys
input = sys.stdin.readline

N, M = map(int, input().split())

removed = 0
edges = set()

for _ in range(M):
    u, v = map(int, input().split())
    if u == v:
        # 自己ループは必ず取り除く
        removed += 1
    else:
        # 辺を (小さい方, 大きい方) の順にして多重辺判定
        a, b = (u, v) if u < v else (v, u)
        if (a, b) in edges:
            # 既に存在する辺は多重辺なので取り除く
            removed += 1
        else:
            edges.add((a, b))

print(removed)