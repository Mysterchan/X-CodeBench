import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()

    # AとBの1の位置リストを作成
    posA = [i for i, c in enumerate(A) if c == '1']
    posB = [i for i, c in enumerate(B) if c == '1']

    # 1の数が違えば不可能
    if len(posA) != len(posB):
        print(-1)
        continue

    # 各コマの移動距離の最大値を求める
    # i番目のコマはposA[i]からposB[i]へ移動
    # 操作回数は最大の移動距離
    max_dist = 0
    for a, b in zip(posA, posB):
        dist = abs(a - b)
        if dist > max_dist:
            max_dist = dist

    print(max_dist)