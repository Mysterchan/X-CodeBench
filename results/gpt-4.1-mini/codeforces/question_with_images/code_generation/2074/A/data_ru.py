t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    # Проверяем условие, при котором точки (-l,0), (r,0), (0,-d), (0,u) образуют квадрат.
    # Для квадрата с такими вершинами должно выполняться:
    # l == r == d == u
    print("Yes" if l == r == d == u else "No")