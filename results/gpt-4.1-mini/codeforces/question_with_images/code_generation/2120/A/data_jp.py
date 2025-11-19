t = int(input())
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())

    # 3つの長方形は回転不可で、l3 ≤ l2 ≤ l1, b3 ≤ b2 ≤ b1

    # 正方形の一辺の長さは l1 または b1 のどちらかである可能性が高い（最大の長方形の辺に合わせる）
    # 3つの長方形を辺に沿って並べて正方形を作る方法は主に2パターン考える:
    # 1) 3つを横に並べる（高さが同じで幅の合計が高さに等しい）
    # 2) 1つを横に置き、残り2つを縦に並べる（またはその逆）

    # ここで、回転不可なので長さと幅は固定

    def can_form_square():
        # パターン1: 3つを横に並べる
        # 高さが同じで、幅の合計が高さに等しい
        if b1 == b2 == b3 and l1 + l2 + l3 == b1:
            return True
        if l1 == l2 == l3 and b1 + b2 + b3 == l1:
            return True

        # パターン2: 1つを横に置き、残り2つを縦に並べる
        # 3つの長方形のうち1つを基準にして、残り2つがその辺に沿って並ぶか確認
        # 例えば、l1 x b1 を基準にして、残り2つを縦に並べる場合
        # l1 == b2 + b3 かつ b1 == l2 == l3 のような形

        # 3つの長方形をそれぞれ基準に試す
        # 1つ目を横に置き、残り2つを縦に並べるパターン
        if l1 == l2 == l3 and b1 == b2 + b3:
            return True
        if b1 == b2 == b3 and l1 == l2 + l3:
            return True

        # 2つ目を横に置き、残り2つを縦に並べるパターン
        if l2 == l1 == l3 and b2 == b1 + b3:
            return True
        if b2 == b1 == b3 and l2 == l1 + l3:
            return True

        # 3つ目を横に置き、残り2つを縦に並べるパターン
        if l3 == l1 == l2 and b3 == b1 + b2:
            return True
        if b3 == b1 == b2 and l3 == l1 + l2:
            return True

        return False

    print("YES" if can_form_square() else "NO")