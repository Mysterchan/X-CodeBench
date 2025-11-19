import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lr = [tuple(map(int, input().split())) for __ in range(n)]

    # 多角形の面積は偶数であることが保証されているので、
    # 半分の面積を求める
    total_area = 0
    for l, r in lr:
        total_area += r - l + 1
    half_area = total_area // 2

    # 凸多角形の定義より、各行は連続区間で表されている。
    # 2つの合同な多角形に分割するには、
    # ある行 k で多角形を上下に分割し、
    # 上半分と下半分が平行移動で一致する必要がある。
    #
    # つまり、ある k (1 <= k < n) が存在して、
    # 上から k 行の面積が半分の面積に等しく、
    # かつ上半分の各行の区間を一定のオフセットで下半分の対応行の区間に一致させられるかを判定する。
    #
    # 具体的には、
    # - 上半分の区間の左端と右端の差を求める
    # - 下半分の対応行の区間と比較し、すべての行で同じオフセットが成り立つか確認する
    #
    # これが成り立てば「YES」、そうでなければ「NO」

    # 累積面積を計算
    prefix_area = [0]
    for l, r in lr:
        prefix_area.append(prefix_area[-1] + (r - l + 1))

    # 半分の面積になる行 k を探す
    # prefix_area[k] == half_area となる k が存在するか
    # 存在しなければ NO
    if half_area not in prefix_area:
        print("NO")
        continue

    k = prefix_area.index(half_area)

    # 上半分と下半分の区間を比較
    # オフセットは上半分の1行目と下半分の1行目の左端の差
    offset = lr[k][0] - lr[0][0]

    # 各行で区間の長さが一致し、左端の差が offset と等しいか確認
    ok = True
    for i in range(k):
        l1, r1 = lr[i]
        l2, r2 = lr[i + k]
        if (r1 - l1) != (r2 - l2) or (l2 - l1) != offset:
            ok = False
            break

    print("YES" if ok else "NO")