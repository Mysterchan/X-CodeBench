T = int(input())
for _ in range(T):
    l, r, d, u = map(int, input().split())
    if l == r and d == u:
        print("Yes")
    else:
        print("No")
