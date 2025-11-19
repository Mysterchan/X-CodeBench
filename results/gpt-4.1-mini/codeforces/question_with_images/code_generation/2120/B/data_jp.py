def main():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        count = 0
        for __ in range(n):
            dx, dy, x, y = map(int, input().split())
            # ボールの軸方向の動きは45度なので、x軸方向とy軸方向の速度は同じ大きさ
            # ポケットは4隅 (0,0), (0,s), (s,0), (s,s)
            # ボールは反射しながら動くが、反射を考慮すると、ボールの動きは「鏡像反射」を繰り返す直線運動とみなせる
            # したがって、ボールがポケットに入るかは、ボールの軌跡上にポケット座標が存在するかどうかで判定可能
            # 具体的には、ボールの動きは (x + t*dx, y + t*dy) だが、壁で反射するときは座標が折り返される
            # 折り返しを考慮すると、ボールの動きは「2s周期の折り返し軌跡」となる
            # そこで、x軸方向とy軸方向の「折り返し後の座標」を考える
            # 折り返し後の座標は、(x + t*dx) mod 2s と (y + t*dy) mod 2s で表される
            # ポケットは (0,0), (0,s), (s,0), (s,s) の4点
            # これらの座標は折り返し後の座標空間で特別な位置にある
            # ボールがポケットに入るとは、あるtで折り返し後の座標がポケット座標と一致すること
            # つまり、(x + t*dx) mod 2s == px かつ (y + t*dy) mod 2s == py となるtが存在するか
            # px, py はポケットの座標のいずれか
            # dx, dy は ±1 なので、tは整数である必要がある
            # これを満たすtが存在するかを判定する

            # 4つのポケットについて判定
            # mod 2s の範囲で考える
            # t ≡ (px - x) * dx (mod 2s)
            # t ≡ (py - y) * dy (mod 2s)
            # これらの合同式が同時に満たされるtが存在するかを判定する

            # dx, dy は ±1 なので、t ≡ (px - x) * dx mod 2s は t ≡ (px - x) * dx mod 2s と同じ
            # ただし、dx = -1 の場合は符号を反転させる

            # 4つのポケット座標
            pockets = [(0,0), (0,s), (s,0), (s,s)]

            # 2sをmとする
            m = 2 * s

            def mod_val(a):
                return a % m

            def solve_congruence(a1, a2, m):
                # a1 ≡ a2 (mod m) の形でtを求める
                # ここではt ≡ a1 (mod m) と t ≡ a2 (mod m) の同時合同式を判定する必要がある
                # しかし、tは1変数で2つの合同式を満たす必要がある
                # つまり、t ≡ r1 (mod m) と t ≡ r2 (mod m) の同時合同式を判定
                # ここではmが同じなので、r1 == r2 なら解あり
                return a1 == a2

            # dx, dy は ±1
            # t ≡ (px - x)*dx mod m
            # t ≡ (py - y)*dy mod m
            # これらが等しいtが存在するか判定

            poted = False
            for px, py in pockets:
                tx = mod_val((px - x) * dx)
                ty = mod_val((py - y) * dy)
                if tx == ty:
                    poted = True
                    break
            if poted:
                count += 1
        print(count)

if __name__ == "__main__":
    main()