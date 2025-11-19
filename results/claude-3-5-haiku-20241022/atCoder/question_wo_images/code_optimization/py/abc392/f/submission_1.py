n = int(input())
p = list(map(int, input().split()))

ans = [0] * n
pos = n - 1

for i in range(n, 0, -1):
    ans[pos] = i
    if i > 1:
        pos -= p[i-2]

print(" ".join(map(str, ans)))