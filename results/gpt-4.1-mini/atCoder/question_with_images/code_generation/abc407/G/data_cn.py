import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 將格子染色成黑白棋盤格，黑格為(i+j)%2==0，白格為1
# 建立二分圖：黑格連接相鄰的白格，邊權為兩格數字和
# 目標：找最大權匹配，使得被骨牌覆蓋的格子數字和最大
# 最終分數 = 全部格子數字和 - 被骨牌覆蓋格子數字和
# 因此最大分數 = sum(A) - 最大匹配權重

# 建立圖
black_nodes = []
black_id = [[-1]*W for _ in range(H)]
white_id = [[-1]*W for _ in range(H)]

b_cnt = 0
w_cnt = 0
for i in range(H):
    for j in range(W):
        if (i+j)%2 == 0:
            black_id[i][j] = b_cnt
            b_cnt += 1
        else:
            white_id[i][j] = w_cnt
            w_cnt += 1

# 建立鄰接表，存邊權
# edges[b] = [(w, weight), ...]
edges = [[] for _ in range(b_cnt)]

# 方向：右、下
directions = [(0,1),(1,0)]

for i in range(H):
    for j in range(W):
        if black_id[i][j] == -1:
            continue
        b = black_id[i][j]
        for dx, dy in directions:
            ni, nj = i+dx, j+dy
            if 0 <= ni < H and 0 <= nj < W:
                if white_id[ni][nj] != -1:
                    w = white_id[ni][nj]
                    weight = A[i][j] + A[ni][nj]
                    edges[b].append((w, weight))

# 最大權匹配 (Maximum Weight Bipartite Matching) - Hungarian Algorithm
# 參考標準實作

INF = 10**15

def hungarian():
    # n = black side count, m = white side count
    n, m = b_cnt, w_cnt
    u = [0]*(n+1)
    v = [0]*(m+1)
    p = [0]*(m+1)
    way = [0]*(m+1)

    for i in range(1, n+1):
        p[0] = i
        j0 = 0
        minv = [INF]*(m+1)
        used = [False]*(m+1)
        while True:
            used[j0] = True
            i0 = p[j0]
            j1 = 0
            delta = INF
            for j in range(1, m+1):
                if not used[j]:
                    # 找邊權 weight
                    # edges[i0-1]中找j-1的weight
                    # 若無邊，weight=0
                    wgt = 0
                    # 用二分搜尋或dict加速
                    # 先用dict
                    # 先建立dict
                    # 但為了效率，先建立edges_dict
                    # 這裡改用edges_dict
                    pass
            # 以上為標準Hungarian模板，需改寫以支援稀疏圖和權重查找

    # 由於標準Hungarian算法為完全二分圖，且本題圖為稀疏圖，
    # 需改寫為稀疏圖版本或用KM算法(Kuhn-Munkres)
    # 下面實作KM算法

def KM():
    n, m = b_cnt, w_cnt
    # 建立權重矩陣，初始化為-∞
    # 由於n,m最大2000，建立n*m矩陣可行
    W_mat = [[-INF]*m for _ in range(n)]
    for i in range(n):
        for w, weight in edges[i]:
            W_mat[i][w] = weight

    lx = [max(row) if max(row) > -INF else 0 for row in W_mat]  # u標籤
    ly = [0]*m  # v標籤
    match = [-1]*m  # v匹配的u

    def dfs(u, visited):
        visited[u] = True
        for v in range(m):
            if slack[v] == 0 and not used[v]:
                used[v] = True
                if match[v] == -1 or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False

    for u in range(n):
        slack = [INF]*m
        while True:
            used = [False]*m
            if dfs(u, [False]*n):
                break
            d = INF
            for v in range(m):
                if not used[v]:
                    d = min(d, slack[v])
            for i2 in range(n):
                if i2 == u or (i2 < n and visited[i2]):
                    lx[i2] -= d
            for j2 in range(m):
                if used[j2]:
                    ly[j2] += d
                else:
                    slack[j2] -= d

    res = 0
    for v in range(m):
        u = match[v]
        if u != -1 and W_mat[u][v] > -INF:
            res += W_mat[u][v]
    return res

# 以上KM實作有誤，需重新實作標準KM算法

# 重新實作KM算法

def km():
    n, m = b_cnt, w_cnt
    W_mat = [[-INF]*m for _ in range(n)]
    for i in range(n):
        for w, weight in edges[i]:
            W_mat[i][w] = weight

    lx = [max(row) if max(row) > -INF else 0 for row in W_mat]
    ly = [0]*m
    match = [-1]*m

    for u in range(n):
        slack = [INF]*m
        prev = [-1]*m
        used_x = [False]*n
        used_y = [False]*m
        queue = []
        queue.append(u)
        used_x[u] = True
        pre = [-1]*m
        while True:
            while queue:
                x = queue.pop(0)
                for y in range(m):
                    if not used_y[y]:
                        tmp = lx[x] + ly[y] - W_mat[x][y]
                        if tmp < slack[y]:
                            slack[y] = tmp
                            pre[y] = x
                        if slack[y] == 0:
                            used_y[y] = True
                            if match[y] == -1:
                                # 找到增廣路
                                cur = y
                                while cur != -1:
                                    prevx = pre[cur]
                                    nxt = match[cur]
                                    match[cur] = prevx
                                    cur = nxt
                                queue.clear()
                                break
                            else:
                                queue.append(match[y])
                                used_x[match[y]] = True
                else:
                    continue
                break
            else:
                d = INF
                for y in range(m):
                    if not used_y[y]:
                        d = min(d, slack[y])
                for i2 in range(n):
                    if used_x[i2]:
                        lx[i2] -= d
                for j2 in range(m):
                    if used_y[j2]:
                        ly[j2] += d
                    else:
                        slack[j2] -= d
                for y in range(m):
                    if not used_y[y] and slack[y] == 0:
                        used_y[y] = True
                        if match[y] == -1:
                            cur = y
                            while cur != -1:
                                prevx = pre[cur]
                                nxt = match[cur]
                                match[cur] = prevx
                                cur = nxt
                            break
                        else:
                            queue.append(match[y])
                            used_x[match[y]] = True
                else:
                    continue
                break
            break

    res = 0
    for y in range(m):
        x = match[y]
        if x != -1 and W_mat[x][y] > -INF:
            res += W_mat[x][y]
    return res

total = 0
for row in A:
    total += sum(row)

ans = total - km()
print(ans)