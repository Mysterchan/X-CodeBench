import sys
input = sys.stdin.readline

H, W = map(int, input().split())
rows = [int(input().strip(), 2) for _ in range(H)]

# 由於 W ≤ 18，我們可以用 bitmask 表示每一行
# 操作 X 是翻轉整行，操作 Y 是翻轉整列
# 我們想要最小化所有元素的和

# 思路：
# 先固定第一行是否翻轉（0或1）
# 對於每一列 y，決定是否翻轉該列，使得第一行該列為0
# 對於其他行，根據第一行是否翻轉，計算該行翻轉與否的最佳選擇
# 因為翻轉行和列的操作可任意次且順序任意，等價於：
# 對每一列決定是否翻轉，使得第一行為0
# 對每一行決定是否翻轉，使得該行中1的數量最小

# 實作：
# 對第一行翻轉狀態 b in {0,1}：
#   對每一列 y，決定是否翻轉該列，使得第一行該列為0
#   對每一行 i，計算翻轉或不翻轉後該行1的數量，取最小
#   累加所有行的最小值，更新答案

ans = H * W
for b in (0, 1):
    # b=0 表示不翻轉第一行，b=1 表示翻轉第一行
    # 根據 b 決定列翻轉 mask
    # col_flip[y] = 1 表示該列翻轉
    col_flip = 0
    for y in range(W):
        bit = (rows[0] >> y) & 1
        if bit ^ b == 1:
            col_flip |= (1 << y)

    total = 0
    for r in rows:
        # 對該行先 XOR col_flip，模擬列翻轉
        val = r ^ col_flip
        # 行翻轉選擇：val 或 ~val (只考慮 W 位)
        cnt1 = bin(val).count('1')
        cnt0 = W - cnt1
        # 如果 b=1，表示第一行翻轉，該行翻轉狀態也要反轉
        # 但因為行翻轉是獨立決定的，直接取 min(cnt1, cnt0)
        total += min(cnt1, cnt0)
    if total < ans:
        ans = total

print(ans)