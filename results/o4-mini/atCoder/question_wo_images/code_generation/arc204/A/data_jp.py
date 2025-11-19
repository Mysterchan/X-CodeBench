import sys
input = sys.stdin.readline

MOD = 998244353

N, L, R = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp[i][j][c]: i番目までの行動1を行い、j個のQの要素が残っている状態で、
# Cの値がcである場合の数
# i: 0..N (行動1をi回行った)
# j: 0..i (Qの長さは最大i)
# c: 0..sumB (Cの値)
# sumB = sum(B)

sumB = sum(B)
maxC = sumB

# dpのメモリ節約のため、2次元配列でcをキーにした辞書を使う
# ただしcは最大 sumB=最大25000程度なので配列で管理可能
# しかしN=5000で3次元はメモリ厳しいので、
# dpは2次元配列でcをキーにした辞書を使うのは遅い。
# ここはcの範囲が最大約25000なので配列で管理可能。
# dp[i][j][c]はi,j,cの3次元配列で、iは1段階ずつ進むので2層で管理可能。

# dp[j][c]: i回目の行動1まで終わった状態でQの長さj、C=cの状態数
dp_prev = [ [0]*(maxC+1) for _ in range(N+1) ]
dp_prev[0][0] = 1

for i in range(N):
    dp_curr = [ [0]*(maxC+1) for _ in range(N+1) ]
    a = A[i]
    b = B[i]
    for j in range(i+1):  # Qの長さは最大i
        for c in range(maxC+1):
            val = dp_prev[j][c]
            if val == 0:
                continue
            # 行動1: Qの末尾にi+1を挿入, C = max(0, c - A[i])
            c1 = c - a
            if c1 < 0:
                c1 = 0
            dp_curr[j+1][c1] = (dp_curr[j+1][c1] + val) % MOD

            # 行動2: Qの先頭の数xに対応するB_xを加算
            # ただしQが空でないときのみ
            if j > 0:
                c2 = c + b
                if c2 <= maxC:
                    dp_curr[j-1][c2] = (dp_curr[j-1][c2] + val) % MOD
    dp_prev = dp_curr

# 最終的にQは空である必要があるのでj=0
# CがL以上R以下の合計を求める
ans = 0
for c in range(L, R+1):
    if c <= maxC:
        ans = (ans + dp_prev[0][c]) % MOD

print(ans)