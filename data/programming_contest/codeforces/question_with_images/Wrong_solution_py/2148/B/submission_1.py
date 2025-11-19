t = int(input())
for _ in range(t):
    x, y, n, m = map(int, input().split())
    a = list(map(int, input().split())) if n > 0 else []
    b = list(map(int, input().split())) if m > 0 else []
    print(n + m)
