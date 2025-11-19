import sys
sys.setrecursionlimit(10**7)

H, W = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

N = H * W

# 將二維座標轉成一維索引
def idx(i, j):
    return i * W + j

# 預先計算所有格子的值
vals = [A[i][j] for i in range(H) for j in range(W)]

# 使用 bitmask 表示哪些格子已被覆蓋
# 狀態空間大小為 2^(H*W)，最大 2^20 約 1百萬，DFS + 記憶化可行

from functools import lru_cache

@lru_cache(None)
def dfs(used):
    # 找第一個未被覆蓋的格子
    if used == (1 << N) - 1:
        # 全部覆蓋，剩餘格子為空，XOR為0
        return 0
    # 找第一個未被覆蓋的格子
    for i in range(N):
        if not (used & (1 << i)):
            break
    else:
        # 全部覆蓋
        return 0

    # 不放多米諾骨牌，該格子保留，XOR加上該格子值
    res = vals[i] ^ dfs(used | (1 << i))

    r, c = divmod(i, W)

    # 嘗試放置水平多米諾骨牌 (i,j) 和 (i,j+1)
    if c + 1 < W:
        j = idx(r, c + 1)
        if not (used & (1 << j)):
            # 放置多米諾骨牌，這兩格都覆蓋，不加值
            res = max(res, dfs(used | (1 << i) | (1 << j)))

    # 嘗試放置垂直多米諾骨牌 (i,j) 和 (i+1,j)
    if r + 1 < H:
        j = idx(r + 1, c)
        if not (used & (1 << j)):
            res = max(res, dfs(used | (1 << i) | (1 << j)))

    return res

print(dfs(0))