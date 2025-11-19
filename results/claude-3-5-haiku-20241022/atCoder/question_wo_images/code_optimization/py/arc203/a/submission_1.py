def pow2(b):
    return 1 << b

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = min(n, m) - 1
    print(pow2(a))