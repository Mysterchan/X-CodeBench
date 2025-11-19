n = int(input())
p = list(map(int, input().split()))

a = []
for i in range(1, n + 1):
    a.insert(p[i - 1] - 1, i)

print(' '.join(map(str, a)))