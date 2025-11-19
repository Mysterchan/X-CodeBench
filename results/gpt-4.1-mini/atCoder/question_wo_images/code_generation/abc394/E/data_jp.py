import sys
input = sys.stdin.readline

N = int(input())
C = [input().rstrip('\n') for _ in range(N)]

INF = 10**9

# dp[i][j]: 最短の回文パスの長さ（辺の数） i->j
# ただし、回文パスは辺のラベルを連結した文字列が回文になるもの
# 長さ0はi==jの空文字列（回文）
dp = [[INF]*N for _ in range(N)]

# 初期化
for i in range(N):
    dp[i][i] = 0  # 空文字列は回文

# 辺が1本で回文になる場合（ラベル1文字は回文）
for i in range(N):
    for j in range(N):
        if C[i][j] != '-':
            dp[i][j] = 1

# ワーシャルフロイド的にdp更新
# 回文の構造を考えると、回文の最短パスは
# 端の文字が同じで、その内側が回文である必要がある
# つまり、i->jの回文パスは
# ある文字cで、i->xにcの辺、y->jにcの辺があり、
# dp[x][y]がわかれば dp[i][j] = dp[x][y] + 2
# これを繰り返す

# 反復回数は最大N^2回程度で十分
for _ in range(N*N):
    updated = False
    for i in range(N):
        for j in range(N):
            # dp[i][j]の更新を試みる
            # すでに0や1ならそれ以下はないのでスキップしても良いが無理に省略しない
            for c in range(N):
                if C[i][c] == '-':
                    continue
                for d in range(N):
                    if C[d][j] == '-':
                        continue
                    if C[i][c] == C[d][j]:
                        cand = dp[c][d] + 2
                        if cand < dp[i][j]:
                            dp[i][j] = cand
                            updated = True
    if not updated:
        break

# 出力
for i in range(N):
    ans = []
    for j in range(N):
        if dp[i][j] == INF:
            ans.append(str(-1))
        else:
            ans.append(str(dp[i][j]))
    print(' '.join(ans))