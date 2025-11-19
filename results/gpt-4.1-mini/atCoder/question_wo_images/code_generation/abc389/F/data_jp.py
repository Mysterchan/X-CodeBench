import sys
input = sys.stdin.readline

N = int(input())
MAX_R = 5 * 10**5

diff = [0] * (MAX_R + 2)  # 差分配列

for _ in range(N):
    L, R = map(int, input().split())
    diff[L] += 1
    diff[R + 1] -= 1

# 差分配列から各レーティングに対する増加回数を計算
for i in range(1, MAX_R + 1):
    diff[i] += diff[i - 1]

Q = int(input())
for _ in range(Q):
    X = int(input())
    # 最終レーティング = 初期レーティング + 増加回数
    print(X + diff[X])