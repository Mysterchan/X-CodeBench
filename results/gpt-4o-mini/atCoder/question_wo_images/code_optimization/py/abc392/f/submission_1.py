n = int(input())
p = list(map(int, input().split()))

ans = [0] * n
available = list(range(1, n + 1))

for i in range(n):
    pos = p[i] - 1
    ans[pos] = available[i]
    available.pop(i)

print(" ".join(map(str, ans)))