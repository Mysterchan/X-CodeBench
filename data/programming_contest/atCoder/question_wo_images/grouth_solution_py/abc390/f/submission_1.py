n = int(input())
a = list(map(int, input().split()))
g = [[] for i in range(n + 1)]
for i in range(n):
    g[a[i] - 1].append(i)

def f(x):
    res = 0
    for i in range(1, len(x)):
        c = x[i] - x[i - 1]
        res += c * (c - 1) // 2
    return res

ans = 0
for i in range(1, n + 1):
    ans += f([-1] + g[i] + [n])
    ans -= f([-1] + sorted(g[i - 1] + g[i]) + [n])
print(ans)