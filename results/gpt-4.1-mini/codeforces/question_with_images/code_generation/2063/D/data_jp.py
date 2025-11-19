import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    k_max = min(n // 2, m)
    if k_max == 0:
        print(0)
        continue

    # 三角形の面積は高さ2なので、底辺の長さの半分 * 2 = 底辺の長さ
    # 操作1回で選ぶ三点は、y=0の2点とy=2の1点
    # 面積 = |x2 - x1| * 2 / 2 = |x2 - x1| (底辺の長さ)
    # よって、面積はy=0の2点の距離の絶対値

    # y=0の点を2点ずつペアにして、y=2の点1点と組み合わせる
    # 面積は底辺の長さ = |a_j - a_i|
    # 最大化するために、y=0の点のペアの距離が大きい順に取り、
    # y=2の点は大きい順に取り、面積を最大化する

    # y=0の点のペアの距離を計算
    # 例えば、aをソート済みなので、a[0], a[1], a[2], a[3], ...
    # ペアは (a[0], a[1]), (a[2], a[3]), ... として距離を計算
    # これらの距離を降順にソートし、bの点のx座標も降順にソートしておく

    # 面積 = (距離) * 2 / 2 = 距離
    # しかし、y=2の点のx座標は面積に影響しない（高さは固定2）
    # つまり、面積は底辺の長さだけで決まる

    # したがって、y=2の点のx座標は面積に影響しないので、
    # 面積は底辺の長さだけで決まる
    # よって、y=2の点はどれを選んでも面積は同じ
    # つまり、y=2の点の数だけ操作回数が制限される

    # よって、k_max = min(n//2, m)
    # f(k) = k回の操作で最大スコア = k回分の最大底辺距離の和

    # y=0の点のペアの距離を計算し、降順にソート
    dist = []
    for i in range(0, 2 * k_max, 2):
        dist.append(abs(a[i+1] - a[i]))
    dist.sort(reverse=True)

    # f(k)はdistの上位k個の和
    res = []
    s = 0
    for i in range(k_max):
        s += dist[i]
        res.append(s)

    print(k_max)
    print(*res)