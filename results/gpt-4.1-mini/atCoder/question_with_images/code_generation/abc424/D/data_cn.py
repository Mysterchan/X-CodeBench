def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        grid = [list(input().strip()) for __ in range(H)]

        # 找出所有黑色格子的位置
        blacks = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == '#']

        # 檢查當前格子狀態是否符合條件
        def valid(state):
            # state 是一個集合，表示被重新塗成白色的黑色格子座標
            # 實際格子顏色 = 原本白色 + 原本黑色但在state中被塗白
            for i in range(H - 1):
                for j in range(W - 1):
                    # 4個格子中是否至少有一個白色
                    # 白色條件：原本是白色，或在state中被塗白
                    cells = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
                    if all((grid[x][y] == '#' and (x, y) not in state) for x, y in cells):
                        return False
            return True

        # 因為H,W最大7，黑色格子最多49，暴力嘗試所有重新塗白的組合
        # 從0個開始嘗試，找到最小值
        from itertools import combinations

        ans = len(blacks)
        for k in range(ans + 1):
            for comb in combinations(blacks, k):
                if valid(set(comb)):
                    ans = k
                    break
            if ans == k:
                break

        print(ans)