import sys
sys.setrecursionlimit(10**7)

H, W = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

N = H * W
vals = [A[i][j] for i in range(H) for j in range(W)]

# 隣接するマスのペア（ドミノ候補）
edges = []
for i in range(H):
    for j in range(W):
        idx = i * W + j
        if j + 1 < W:
            edges.append((idx, idx + 1))
        if i + 1 < H:
            edges.append((idx, idx + W))

# メモ化用辞書
memo = {}

def dfs(used_mask, pos):
    if pos == len(edges):
        # 置かれていないマスのXORを計算
        res = 0
        for i in range(N):
            if (used_mask >> i) & 1 == 0:
                res ^= vals[i]
        return res

    key = (used_mask, pos)
    if key in memo:
        return memo[key]

    u, v = edges[pos]
    res = dfs(used_mask, pos + 1)  # このドミノを置かない場合

    # このドミノを置う場合（両方のマスが未使用なら）
    if ((used_mask >> u) & 1) == 0 and ((used_mask >> v) & 1) == 0:
        res = max(res, dfs(used_mask | (1 << u) | (1 << v), pos + 1))

    memo[key] = res
    return res

print(dfs(0, 0))