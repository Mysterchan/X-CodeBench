import sys
import bisect

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 水平レーザーのうち、y座標yより小さいものの個数
    h_count = bisect.bisect_left(a, y)
    # 垂直レーザーのうち、x座標xより小さいものの個数
    v_count = bisect.bisect_left(b, x)

    # 最小交差数はそれぞれのレーザーを越える回数の合計
    print(h_count + v_count)