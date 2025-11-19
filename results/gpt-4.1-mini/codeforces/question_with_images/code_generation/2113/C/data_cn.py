import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    grid = [input().strip() for __ in range(n)]

    # 建立金子前綴和
    # gold[i][j] 表示 (0,0) 到 (i-1,j-1) 的金子數量
    gold = [[0]*(m+1) for __ in range(n+1)]
    for i in range(n):
        for j in range(m):
            gold[i+1][j+1] = gold[i+1][j] + gold[i][j+1] - gold[i][j] + (1 if grid[i][j] == 'g' else 0)

    def get_gold(x1, y1, x2, y2):
        # 返回區域內金子數量，區域邊界包含
        if x1 > x2 or y1 > y2:
            return 0
        x1 = max(x1, 0)
        y1 = max(y1, 0)
        x2 = min(x2, n-1)
        y2 = min(y2, m-1)
        if x1 > x2 or y1 > y2:
            return 0
        return gold[x2+1][y2+1] - gold[x1][y2+1] - gold[x2+1][y1] + gold[x1][y1]

    max_gold = 0
    for x in range(n):
        for y in range(m):
            if grid[x][y] == '.':
                # 爆炸中心(x,y)
                # 邊長 = 2k+1
                # 邊界範圍
                top = x - k
                bottom = x + k
                left = y - k
                right = y + k

                # 邊界上的金子數量 = 總金子數 - 內部金子數
                total = get_gold(top, left, bottom, right)
                inner = get_gold(top+1, left+1, bottom-1, right-1)
                border_gold = total - inner
                if border_gold > max_gold:
                    max_gold = border_gold

    print(max_gold)