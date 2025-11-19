def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        grid = [list(input().rstrip()) for __ in range(H)]

        # 条件を満たすために白に変えるべき黒マスの最小数を求める
        # 2x2の黒マスの塊が存在しないようにする
        # 2x2の黒マスの塊がある場合、そこから少なくとも1つは白に変える必要がある
        # 2x2の黒マスの塊をすべて壊すために必要な最小の黒マスの白変換数を求める問題

        # 黒マスの位置をリストアップ
        black_positions = []
        pos_to_idx = {}
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '#':
                    pos_to_idx[(i, j)] = len(black_positions)
                    black_positions.append((i, j))

        n = len(black_positions)
        # 2x2の黒マスの塊をリストアップ
        blocks = []
        for i in range(H - 1):
            for j in range(W - 1):
                # 4マスがすべて黒か？
                if (grid[i][j] == '#' and grid[i][j+1] == '#' and
                    grid[i+1][j] == '#' and grid[i+1][j+1] == '#'):
                    # この4マスのインデックスを取得
                    block = []
                    block.append(pos_to_idx[(i, j)])
                    block.append(pos_to_idx[(i, j+1)])
                    block.append(pos_to_idx[(i+1, j)])
                    block.append(pos_to_idx[(i+1, j+1)])
                    blocks.append(block)

        # blocksの各要素は、4つの黒マスのインデックスのリスト
        # これらのブロックをすべて壊すために、各ブロックから少なくとも1つのマスを白に変える必要がある
        # つまり、blocksの各集合に対して少なくとも1つの要素を選ぶ集合被覆問題
        # ここで、選ぶ要素は黒マスのインデックスで、選んだ黒マスは白に変えることを意味する
        # 最小の選択数を求める

        # n <= 49 (最大7*7=49)
        # blocksの数は最大36 (6*6)
        # bitmaskで全探索は2^nで大きすぎる
        # blocksの数は最大36なので、ブロックを満たすかどうかをbitmaskで管理し、
        # 黒マスの選択でどのブロックを壊せるかを計算し、最小の選択数を求める

        # 各黒マスが壊せるブロックのbitを計算
        m = len(blocks)
        black_cover = [0] * n
        for b_idx, block in enumerate(blocks):
            for pos_idx in block:
                black_cover[pos_idx] |= (1 << b_idx)

        # 全ブロックを壊すためのbitmask
        full_mask = (1 << m) - 1

        # DPで最小選択数を求める
        # dp[mask] = 黒マスの白変換で壊したブロックの集合maskに対する最小選択数
        # maskは壊したブロックのbitmask
        from collections import deque

        dp = [float('inf')] * (1 << m)
        dp[0] = 0
        queue = deque([0])

        while queue:
            mask = queue.popleft()
            cost = dp[mask]
            if mask == full_mask:
                break
            for i in range(n):
                new_mask = mask | black_cover[i]
                if dp[new_mask] > cost + 1:
                    dp[new_mask] = cost + 1
                    queue.append(new_mask)

        # blocksが0個なら0
        ans = dp[full_mask] if m > 0 else 0
        print(ans)

if __name__ == "__main__":
    main()