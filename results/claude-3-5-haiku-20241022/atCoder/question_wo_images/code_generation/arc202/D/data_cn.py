H, W, T, A, B, C, D = map(int, input().split())

MOD = 998244353

# 8个方向
directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

# 使用两个字典进行滚动
prev = {}
prev[(A, B)] = 1

for step in range(T):
    curr = {}
    
    for (i, j), count in prev.items():
        # 尝试移动到8个相邻位置
        for di, dj in directions:
            ni, nj = i + di, j + dj
            # 检查是否在棋盘内
            if 1 <= ni <= H and 1 <= nj <= W:
                if (ni, nj) not in curr:
                    curr[(ni, nj)] = 0
                curr[(ni, nj)] = (curr[(ni, nj)] + count) % MOD
    
    prev = curr

# 输出答案
print(prev.get((C, D), 0))