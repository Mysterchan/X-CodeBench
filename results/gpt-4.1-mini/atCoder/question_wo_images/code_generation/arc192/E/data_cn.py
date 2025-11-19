MOD = 998244353

# 預先計算階乘與反階乘用於組合數計算
MAX = 2_000_000  # W,H最大10^6，x+y最大約2*10^6
fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

def modinv(a, m=MOD):
    # 費馬小定理求逆元 (m為質數)
    return pow(a, m - 2, m)

def prepare_factorials():
    for i in range(1, MAX + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[MAX] = modinv(fact[MAX], MOD)
    for i in range(MAX - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def paths(x1, y1, x2, y2):
    # 從(x1,y1)走到(x2,y2)只能往右或往上，計算路徑數
    dx = x2 - x1
    dy = y2 - y1
    if dx < 0 or dy < 0:
        return 0
    return comb(dx + dy, dx)

def main():
    import sys
    sys.setrecursionlimit(10**7)
    W, H, L, R, D, U = map(int, sys.stdin.readline().split())

    prepare_factorials()

    # 區塊分佈：
    # (x,y) 0<=x<=W, 0<=y<=H
    # 且 x<L or x>R or y<D or y>U 才有區塊
    # 意即中間矩形 [L,R]x[D,U] 沒有區塊

    # Snuke可從任一區塊起點開始，且只能往右或往上走，且走到的點必須是區塊

    # 我們要計算所有從任意區塊起點出發，往右或往上走，且路徑上的點都在區塊上的路徑數總和。

    # 觀察：
    # 區塊分成四個區域：
    # 左區域: x < L, y in [0,H]
    # 右區域: x > R, y in [0,H]
    # 下區域: y < D, x in [0,W]
    # 上區域: y > U, x in [0,W]

    # 這四個區域互相不連通（因為中間矩形空缺），
    # 但上下左右區域會有重疊區域（例如左下角區域 x<L且y<D）

    # 但路徑只能往右或往上走，且路徑上的點都必須是區塊。
    # 因此路徑只能在同一個連通區域內。

    # 連通區域有四個：
    # 1) 左下區域: x<L且y<D
    # 2) 左上區域: x<L且y>U
    # 3) 右下區域: x>R且y<D
    # 4) 右上區域: x>R且y>U

    # 另外還有純左區域( x<L且D<=y<=U )，純右區域( x>R且D<=y<=U )，
    # 純下區域( L<=x<=R且y<D )，純上區域( L<=x<=R且y>U )，
    # 這些區域是連續的，但因為中間矩形空缺，這些區域是分開的。

    # 但因為路徑只能往右或往上，且必須在區塊上，
    # 這些區域中，只有四個角落區域是連通的（因為中間矩形空缺阻斷了中間部分）

    # 但題目中區塊定義是 x<L or x>R or y<D or y>U
    # 這是四個條件的聯集，區塊是四個區域的聯集：
    # 左區域: x<L, y in [0,H]
    # 右區域: x>R, y in [0,H]
    # 下區域: y<D, x in [0,W]
    # 上區域: y>U, x in [0,W]

    # 這四個區域彼此有重疊，且路徑只能往右或往上，
    # 因此路徑只能在同一個區域內，且起點和終點都在該區域。

    # 因此，我們可以分別計算在這四個區域中所有可能路徑數，最後相加。

    # 計算方法：
    # 對於一個區域，所有點是格點集合，
    # 路徑是從任意點出發，往右或往上走，且路徑上的點都在該區域。

    # 計算該區域所有路徑數：
    # 先計算該區域所有點對(x1,y1)->(x2,y2)的路徑數，x1<=x2,y1<=y2，
    # 並且路徑上的點都在該區域。

    # 由於路徑只能往右或往上，且區域是矩形或長條形，
    # 路徑上的點都在區域內，等同於x1,y1,x2,y2都在區域內。

    # 因此，該區域所有路徑數 = sum_{(x1,y1),(x2,y2)} paths(x1,y1,x2,y2)
    # 其中(x1,y1)和(x2,y2)在區域內，且x1<=x2,y1<=y2。

    # 計算所有路徑數的技巧：
    # 對區域內所有點排序（按x,y），
    # 路徑數 = sum_{x1<=x2,y1<=y2} C((x2 - x1)+(y2 - y1), x2 - x1)

    # 這個計算量太大，需用數學公式化簡。

    # 觀察：
    # 對一維區間[0,n]，所有路徑數從任意點到任意點往右或往上，
    # 等同於計算所有區間的組合數和。

    # 但本題區域是矩形或長條形。

    # 先分別計算四個區域的路徑數：

    # 1) 左區域: x in [0,L-1], y in [0,H]
    # 2) 右區域: x in [R+1,W], y in [0,H]
    # 3) 下區域: x in [0,W], y in [0,D-1]
    # 4) 上區域: x in [0,W], y in [U+1,H]

    # 這四個區域的交集是空的（因為x區間不重疊或y區間不重疊）

    # 因此總路徑數 = sum(四個區域路徑數) - sum(兩兩交集路徑數) + sum(三重交集路徑數) - 四重交集路徑數

    # 但四個區域的交集是空的，因為x區間和y區間不重疊，
    # 只有兩兩交集可能存在：
    # 左區域與下區域交集: x in [0,L-1], y in [0,D-1]
    # 左區域與上區域交集: x in [0,L-1], y in [U+1,H]
    # 右區域與下區域交集: x in [R+1,W], y in [0,D-1]
    # 右區域與上區域交集: x in [R+1,W], y in [U+1,H]

    # 這四個交集區域是矩形。

    # 三重交集和四重交集不存在（因為x區間不重疊）

    # 因此用容斥原理：
    # 答案 = sum(四個區域路徑數) - sum(四個交集區域路徑數)

    # 計算一個矩形區域內所有路徑數：
    # 區域: x in [x1,x2], y in [y1,y2]
    # 點數: (x2 - x1 + 1)*(y2 - y1 + 1)
    # 所有路徑數 = sum_{x1<=a<=b<=x2} sum_{y1<=c<=d<=y2} paths(a,c,b,d)
    # paths(a,c,b,d) = C((b - a) + (d - c), b - a)

    # 令 X = x2 - x1 + 1, Y = y2 - y1 + 1
    # 我們要計算 sum_{0<=dx<X} sum_{0<=dy<Y} (X - dx)*(Y - dy)*C(dx+dy, dx)
    # 其中 dx = b - a, dy = d - c

    # 因為對每個dx,dy，有 (X - dx)*(Y - dy) 個起點對應該距離

    # 計算公式：
    # total = sum_{dx=0}^{X-1} sum_{dy=0}^{Y-1} (X - dx)*(Y - dy)*C(dx+dy, dx)

    # 預先計算組合數，然後計算此雙重和。

    # 實作此計算。

    def rect_paths(x1, x2, y1, y2):
        if x2 < x1 or y2 < y1:
            return 0
        X = x2 - x1 + 1
        Y = y2 - y1 + 1
        res = 0
        for dx in range(X):
            for dy in range(Y):
                ways = comb(dx + dy, dx)
                count = (X - dx) * (Y - dy)
                res += ways * count
        return res % MOD

    # 四個區域
    left_area = rect_paths(0, L - 1, 0, H) if L > 0 else 0
    right_area = rect_paths(R + 1, W, 0, H) if R < W else 0
    down_area = rect_paths(0, W, 0, D - 1) if D > 0 else 0
    up_area = rect_paths(0, W, U + 1, H) if U < H else 0

    # 四個交集區域
    left_down = rect_paths(0, L - 1, 0, D - 1) if L > 0 and D > 0 else 0
    left_up = rect_paths(0, L - 1, U + 1, H) if L > 0 and U < H else 0
    right_down = rect_paths(R + 1, W, 0, D - 1) if R < W and D > 0 else 0
    right_up = rect_paths(R + 1, W, U + 1, H) if R < W and U < H else 0

    ans = (left_area + right_area + down_area + up_area) % MOD
    ans -= (left_down + left_up + right_down + right_up)
    ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()