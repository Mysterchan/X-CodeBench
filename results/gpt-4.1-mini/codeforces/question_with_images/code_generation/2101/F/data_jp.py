import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 998244353

# 3^n mod
def mod_pow3(n):
    res = 1
    base = 3
    while n > 0:
        if n & 1:
            res = res * base % MOD
        base = base * base % MOD
        n >>= 1
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    edges = [[] for __ in range(n)]
    for __ in range(n-1):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    # 全頂点間距離を求める
    # 木なので BFS n回で O(n^2) = 9*10^6程度で間に合う
    dist = [[-1]*n for __ in range(n)]
    from collections import deque
    for i in range(n):
        dist[i][i] = 0
        q = deque([i])
        while q:
            cur = q.popleft()
            for nx in edges[cur]:
                if dist[i][nx] == -1:
                    dist[i][nx] = dist[i][cur] + 1
                    q.append(nx)

    # d=0..max_dist で距離ごとに辺のペア数を数える
    max_dist = 0
    count = [0]*(n)  # 距離dのペア数
    for i in range(n):
        for j in range(i+1,n):
            d = dist[i][j]
            count[d] += 1
            if d > max_dist:
                max_dist = d

    # 3^n mod
    pow3 = [1]*(n+1)
    for i in range(1,n+1):
        pow3[i] = pow3[i-1]*3 % MOD

    # クールさの合計を求める
    # すべての彩色の数は 3^n
    # クールさ = 赤と青の最大距離
    # 赤がいない or 青がいない => クールさ=0
    # 距離d以上のペアが赤青である彩色数を考える
    # 距離d以上のペアが赤青である彩色数 = 3^n - 2*2^n + 1
    # ただし、2^nは赤または青がいない彩色数
    # しかし、距離d以上のペアが赤青である彩色数は
    # 距離d以上のペアの頂点集合を考慮しないといけないので
    # ここでは距離d以上のペアの頂点集合を使うのは難しい
    #
    # 代わりに、距離dのペアが赤青である彩色数を考える
    # クールさがdである彩色数 = 距離d以上のペアが赤青である彩色数 - 距離d+1以上のペアが赤青である彩色数
    #
    # 距離d以上のペアが赤青である彩色数は以下のように計算できる
    # 距離d以上のペアの頂点集合をVdとする
    # Vdの頂点数をvdとすると
    # 距離d以上のペアが赤青である彩色数 = 3^n - 2*2^vd + 1
    #
    # しかし、Vdの頂点集合を求めるのは難しい
    #
    # そこで、距離dのペアが赤青である彩色数を直接計算する方法を考える
    #
    # 距離dのペアはcount[d]個ある
    # それぞれのペア(u,v)について
    # 赤がu, 青がv または 赤がv, 青がu の2通りの色の割り当てがある
    # 他の頂点は白か赤か青かの3通り
    # ただし、赤と青は少なくとも1つずつ存在しなければならない
    #
    # しかし、複数ペアがあるので重複を考慮しなければならない
    #
    # ここで、クールさの合計は
    # sum_{d=1}^{max_dist} d * (クールさがdの彩色数)
    #
    # クールさがdの彩色数 = 距離d以上のペアが赤青である彩色数 - 距離d+1以上のペアが赤青である彩色数
    #
    # 距離d以上のペアが赤青である彩色数は
    # 3^n - 2 * 2^{n - S_d} + 1
    # ここでS_dは距離d以上のペアの頂点集合の補集合のサイズ
    #
    # しかし、S_dを求めるのは難しい
    #
    # 代わりに、距離dのペアが赤青である彩色数を考える
    #
    # 距離dのペアが赤青である彩色数 = 2 * count[d] * 3^{n-2}
    #
    # これは、距離dのペア(u,v)を赤青に固定し、他の頂点は自由に3色に塗る場合の数
    #
    # しかし、これだとクールさがd以上の彩色数の重複カウントになる
    #
    # そこで Inclusion-Exclusion を使う
    #
    # クールさの合計 = sum_{d=1}^{max_dist} d * (距離d以上のペアが赤青である彩色数 - 距離d+1以上のペアが赤青である彩色数)
    #
    # 距離d以上のペアが赤青である彩色数 = 3^n - 2 * 2^{n - |V_d|} + 1
    #
    # ここで、V_dは距離d以上のペアの頂点集合
    #
    # V_dのサイズを求めるために、距離d以上のペアの頂点集合を求める
    #
    # しかし、距離d以上のペアの頂点集合は
    # 距離d以上のペアの頂点集合 = {頂点v | vは距離d以上のペアのどちらかの頂点}
    #
    # つまり、距離d以上のペアの頂点集合は、距離d以上のペアの端点の集合
    #
    # これを求めるには、距離d以上のペアを列挙し、その端点を集める
    #
    # これをd=1..max_distで行うと O(n^2)で可能
    #
    # まとめると
    # クールさの合計 = sum_{d=1}^{max_dist} d * (f(d) - f(d+1))
    # ただし f(d) = 3^n - 2 * 2^{n - |V_d|} + 1
    #
    # |V_d|は距離d以上のペアの端点集合のサイズ
    #
    # これを計算して出力する

    # 距離d以上のペアの端点集合のサイズを求める
    # まず距離d以上のペアを集める
    # 端点集合をbitsetで管理すると高速化できるがPythonではsetで代用
    # O(n^2)で十分

    # 距離d以上のペアの端点集合のサイズを配列で保持
    Vd_size = [0]*(max_dist+2)  # max_dist+1まで使うので+2

    # 距離d以上のペアの端点集合を求めるために距離d以上のペアを集める
    # まず距離dのペアの端点集合を作る
    # そこから距離d以上の端点集合を作るために累積和的に処理

    # 距離dのペアの端点集合を作る
    # 各距離dについて端点集合をセットで保持
    dist_points = [set() for __ in range(max_dist+1)]
    for i in range(n):
        for j in range(i+1,n):
            d = dist[i][j]
            dist_points[d].add(i)
            dist_points[d].add(j)

    # 距離d以上の端点集合を作る
    # max_distから1に向かって累積和的にセットを合成
    Vd_set = set()
    for d in range(max_dist, 0, -1):
        Vd_set |= dist_points[d]
        Vd_size[d] = len(Vd_set)
    # d = max_dist+1 は空集合
    Vd_size[max_dist+1] = 0

    # 2^k mod 計算用
    pow2 = [1]*(n+1)
    for i in range(1,n+1):
        pow2[i] = pow2[i-1]*2 % MOD

    ans = 0
    pow3_n = pow3[n]
    for d in range(1, max_dist+1):
        f_d = (pow3_n - 2 * pow2[n - Vd_size[d]] + 1) % MOD
        f_d1 = (pow3_n - 2 * pow2[n - Vd_size[d+1]] + 1) % MOD
        val = (f_d - f_d1) % MOD
        ans += d * val
    ans %= MOD

    print(ans)