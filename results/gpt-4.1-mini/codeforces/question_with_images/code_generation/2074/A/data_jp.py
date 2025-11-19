t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    # 正方形の条件は、4つの点が正方形の頂点であること
    # 与えられた点は (-l,0), (r,0), (0,-d), (0,u)
    # 正方形の辺の長さは等しく、内角は90度
    # この4点が正方形の頂点になるのは、l == r == d == u のときのみ
    print("Yes" if l == r == d == u else "No")