import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, x, y, vx, vy = map(int, input().split())

        # 反射を考慮した飛行機の動きを、三角形の鏡像を使って直線運動に変換する。
        # 三角形の頂点は (0,0), (0,n), (n,0)
        # 飛行機は内部にあり、x,y > 0, x+y < n
        # 速度は正の整数

        # 反射を考慮すると、x軸方向は0〜nの区間で反射し、y軸方向も同様。
        # 斜辺は x+y = n で反射。これが難しい部分。

        # 斜辺の反射は速度ベクトルの (vx, vy) を (vy, vx) に入れ替えることで表現できる。
        # つまり、斜辺に当たると vx と vy が入れ替わる。

        # 境界に当たると速度ベクトルの対応する成分が反転する。
        # x=0 または x=n の境界で vx -> -vx
        # y=0 または y=n の境界で vy -> -vy
        # 斜辺 x+y=n の境界で vx, vy を入れ替える。

        # これらの反射を考慮した運動は周期的になる。
        # 頂点に到達する条件は、ある時刻 t で (x_t, y_t) が (0,0), (0,n), (n,0) のいずれかになること。

        # 速度は正なので、反射で符号が変わることを考慮し、速度の絶対値を使う。
        # 反射のたびに符号や vx, vy の入れ替えが起こる。

        # ここで重要なのは、頂点に到達する時刻 t は整数倍の周期で現れるかどうか。

        # 速度の絶対値を使い、x方向の周期は 2*n, y方向の周期も 2*n。
        # 斜辺の反射は vx, vy の入れ替えで、これが周期的に起こる。

        # 速度ベクトルの変化は vx, vy の入れ替えと符号反転の組み合わせで、
        # 速度ベクトルの状態は最大8通り（符号と入れ替えの組み合わせ）で周期的に繰り返す。

        # したがって、最大8回の反射で速度ベクトルの状態は元に戻る。

        # これを利用して、最大8回の速度ベクトルの状態をシミュレーションし、
        # 各状態で頂点に到達可能か判定する。

        # 位置の変化は t 秒後に
        # x_t = x + vx * t
        # y_t = y + vy * t
        # ただし、反射により vx, vy は符号や入れ替えが変わる。

        # 反射のたびに速度ベクトルを更新し、頂点に到達する t を求める。

        # 反射回数をカウントし、最小の衝突回数を出力。

        # 反射の種類:
        # 1. x=0 または x=n で vx -> -vx
        # 2. y=0 または y=n で vy -> -vy
        # 3. x+y=n で vx, vy 入れ替え

        # 速度ベクトルの状態は (vx, vy) または (vy, vx) の符号付き組み合わせで8通り。

        # 反射回数は境界に当たる回数。頂点到達時はカウントしない。

        # まず、頂点に到達する t を求める方法を考える。

        # 頂点は (0,0), (0,n), (n,0)
        # t 秒後の位置は (x_t, y_t) = (x + vx*t, y + vy*t)
        # ただし、反射により vx, vy は変化する。

        # 反射を考慮しないと、頂点に到達する t は存在しない（初期条件で内部にいるため）。

        # 反射を考慮した運動は、鏡像法で考えると、x方向は周期 2*n、y方向も周期 2*n の直線運動に変換できる。

        # 斜辺の反射は vx, vy の入れ替えなので、これも周期的に起こる。

        # したがって、鏡像空間での位置は
        # X(t) = x + vx * t (mod 2*n)
        # Y(t) = y + vy * t (mod 2*n)
        # ただし、斜辺の反射は vx, vy の入れ替えで考慮。

        # 斜辺の反射は vx, vy の入れ替えなので、速度ベクトルの状態は8通り。

        # これらの状態を順にシミュレーションし、頂点に到達する t を求める。

        # 具体的には、速度ベクトルの状態を (vx, vy) の符号と入れ替えの組み合わせで表し、
        # 各状態で頂点に到達する t を計算。

        # 速度ベクトルの状態遷移は以下の通り:
        # 反射回数をカウントしながら、状態を変化させる。

        # 反射の種類は境界に当たるたびに起こる。

        # ここで、問題の制約が大きいので、シミュレーションはできない。

        # したがって、数学的に解く。

        # 重要なポイントは、頂点に到達する t は整数であり、
        # 位置が頂点になる条件は以下のいずれか:

        # (1) x_t = 0 and y_t = 0
        # (2) x_t = 0 and y_t = n
        # (3) x_t = n and y_t = 0

        # ただし、x_t, y_t は反射を考慮した位置。

        # 反射を考慮した位置は、鏡像法で考えると、
        # x方向の鏡像座標 X' = x + vx * t mod 2*n
        # y方向の鏡像座標 Y' = y + vy * t mod 2*n

        # ただし、鏡像座標から実座標への変換は、
        # X = X' if X' <= n else 2*n - X'
        # Y = Y' if Y' <= n else 2*n - Y'

        # 斜辺の反射は vx, vy の入れ替えなので、鏡像空間での運動は
        # 速度ベクトルの入れ替えを考慮しないといけない。

        # しかし、斜辺の反射は vx, vy の入れ替えなので、
        # 鏡像空間での運動は (X', Y') = (x + vx * t, y + vy * t) mod 2*n で表せるが、
        # 斜辺の反射は速度ベクトルの入れ替えなので、鏡像空間での運動は
        # 速度ベクトルの入れ替えを考慮した周期的な運動になる。

        # ここで、斜辺の反射は vx, vy の入れ替えなので、
        # 速度ベクトルの状態は8通りで周期的に繰り返す。

        # したがって、最大8回の反射で速度ベクトルの状態は元に戻る。

        # これを利用して、最大8回の反射までシミュレーションし、
        # 各状態で頂点に到達する t を計算。

        # 反射回数は境界に当たる回数。

        # 反射の種類は以下の優先順位で起こる:
        # 1. x=0 or x=n で vx反転
        # 2. y=0 or y=n で vy反転
        # 3. x+y=n で vx, vy 入れ替え

        # しかし、問題文の例から、斜辺の反射は速度ベクトルの入れ替えのみで符号反転はない。

        # したがって、反射のたびに速度ベクトルの状態を更新し、
        # 位置を更新しながら頂点に到達するか判定。

        # しかし、t は連続値なので、反射時刻を計算し、次の反射までの時間を求める。

        # 反射時刻は各境界までの時間の最小値。

        # これを繰り返し、頂点に到達するか判定。

        # ただし、t は整数でなくてもよい（問題文に整数制限なし）。

        # しかし、頂点に到達する時刻は実数でよい。

        # 反射回数は境界に当たる回数。

        # これを実装。

        # 反射時刻の計算:
        # x方向の次の反射時刻:
        #   if vx > 0: tx = (boundary_x - x) / vx
        #   if vx < 0: tx = (x - boundary_x) / -vx
        # y方向も同様。

        # 斜辺の反射時刻は (x + y) = n となる t:
        #   t = (n - x - y) / (vx + vy)  (vx+vy > 0)

        # これらの中で最小の正の t が次の反射時刻。

        # 反射時刻で位置を更新し、速度ベクトルを反射させる。

        # 頂点に到達したら終了。

        # 反射回数をカウント。

        # 反射回数が一定回数を超えたら -1 とする（無限ループ防止）。

        # 実装開始。

        # 初期位置と速度
        px, py = x, y
        vx_cur, vy_cur = vx, vy
        collisions = 0

        # 反射回数上限（8状態周期 × 10回程度余裕）
        MAX_COLLISIONS = 100

        def is_vertex(x, y):
            return (x == 0 and y == 0) or (x == 0 and y == n) or (x == n and y == 0)

        # 反射判定用の境界座標
        # x=0 or x=n
        # y=0 or y=n
        # x+y=n

        # 速度は常に正か負かで符号を持つ

        # 反射時刻計算関数
        def next_reflection_time(px, py, vx, vy):
            times = []

            # x=0 or x=n
            if vx > 0:
                tx = (n - px) / vx
                if tx > 1e-15:
                    times.append((tx, 'x'))
            elif vx < 0:
                tx = (0 - px) / vx
                if tx > 1e-15:
                    times.append((tx, 'x'))

            # y=0 or y=n
            if vy > 0:
                ty = (n - py) / vy
                if ty > 1e-15:
                    times.append((ty, 'y'))
            elif vy < 0:
                ty = (0 - py) / vy
                if ty > 1e-15:
                    times.append((ty, 'y'))

            # x+y = n
            denom = vx + vy
            if denom != 0:
                t_diag = (n - px - py) / denom
                if t_diag > 1e-15:
                    times.append((t_diag, 'd'))

            if not times:
                return None, None
            return min(times, key=lambda x: x[0])

        # 頂点に到達するか判定
        def reached_vertex(px, py):
            # 浮動小数点誤差を考慮し、十分小さい誤差で判定
            eps = 1e-15
            candidates = [(0,0), (0,n), (n,0)]
            for vx_, vy_ in candidates:
                if abs(px - vx_) < eps and abs(py - vy_) < eps:
                    return True
            return False

        # 初期位置が頂点なら衝突0で脱出可能
        if is_vertex(px, py):
            print(0)
            continue

        # シミュレーション開始
        ans = -1
        for _ in range(MAX_COLLISIONS):
            # 頂点に到達していれば終了
            if reached_vertex(px, py):
                ans = collisions
                break

            t, boundary = next_reflection_time(px, py, vx_cur, vy_cur)
            if t is None:
                # これ以上反射しないなら脱出不可
                break

            # 反射前に頂点に到達するか判定
            # 頂点は境界上にあるので、反射時刻の直前に頂点にいる可能性はない
            # しかし、tの間に頂点に到達するかは線形なので、
            # t秒後の位置を計算し、頂点か判定

            nx = px + vx_cur * t
            ny = py + vy_cur * t

            if reached_vertex(nx, ny):
                ans = collisions
                break

            # 反射回数増加
            collisions += 1

            # 反射後の速度更新
            if boundary == 'x':
                vx_cur = -vx_cur
            elif boundary == 'y':
                vy_cur = -vy_cur
            else:  # boundary == 'd' 斜辺反射
                vx_cur, vy_cur = vy_cur, vx_cur

            # 位置更新
            px, py = nx, ny

        else:
            # ループ終了後も頂点に到達していなければ -1
            if reached_vertex(px, py):
                ans = collisions
            else:
                ans = -1

        print(ans)

solve()