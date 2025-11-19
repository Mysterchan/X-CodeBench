t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    # 判斷是否為正方形：四個點分別為 (-l,0), (r,0), (0,-d), (0,u)
    # 正方形條件：l == r == d == u
    print("Yes" if l == r == d == u else "No")