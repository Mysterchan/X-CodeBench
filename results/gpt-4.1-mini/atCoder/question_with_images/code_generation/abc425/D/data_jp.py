import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    # 黒マスの隣接黒マス数を管理するための配列
    black = [[False]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                black[i][j] = True

    # 各白マスに隣接する黒マスの数をカウント
    adj_black_count = [[0]*W for _ in range(H)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for i in range(H):
        for j in range(W):
            if black[i][j]:
                for dx, dy in directions:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < H and 0 <= ny < W and not black[nx][ny]:
                        adj_black_count[nx][ny] += 1

    # 操作対象となる白マスをキューに入れる
    q = deque()
    for i in range(H):
        for j in range(W):
            if not black[i][j] and adj_black_count[i][j] == 1:
                q.append((i,j))

    # BFS的に操作を繰り返す
    while q:
        i, j = q.popleft()
        if black[i][j]:
            continue
        black[i][j] = True
        # 黒くなったことで隣接白マスのadj_black_countを更新
        for dx, dy in directions:
            nx, ny = i+dx, j+dy
            if 0 <= nx < H and 0 <= ny < W and not black[nx][ny]:
                adj_black_count[nx][ny] += 1
                # ちょうど1つの黒隣接マスを持つ白マスが新たにできたらキューに追加
                if adj_black_count[nx][ny] == 1:
                    q.append((nx, ny))

    # 黒マスの数を数える
    ans = sum(black[i][j] for i in range(H) for j in range(W))
    print(ans)

if __name__ == "__main__":
    main()