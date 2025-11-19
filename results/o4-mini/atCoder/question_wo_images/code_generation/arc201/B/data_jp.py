import sys
input = sys.stdin.readline

T = int(input())
# 全テストケースのNの総和は2*10^5以下なので、各テストケースでX_iごとに最大価値を求めて、
# それらを重みの小さい順に貪欲に選べばよい。

for _ in range(T):
    N, W = map(int, input().split())
    max_value = [0]*60  # X_i < 60なので60個のバケット
    for __ in range(N):
        x, y = map(int, input().split())
        if y > max_value[x]:
            max_value[x] = y

    ans = 0
    # 重みは2^xなので、重みの小さい順に価値の大きいものを選ぶ
    # Wが大きいので、2^x <= Wのときだけ選べる
    for x in range(60):
        w = 1 << x
        if w <= W and max_value[x] > 0:
            ans += max_value[x]
            W -= w
            if W < 0:
                break
    print(ans)