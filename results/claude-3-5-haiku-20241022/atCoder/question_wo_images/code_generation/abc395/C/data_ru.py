n = int(input())
a = list(map(int, input().split()))

min_length = float('inf')

for i in range(n):
    seen = {}
    for j in range(i, n):
        if a[j] in seen:
            min_length = min(min_length, j - i + 1)
            break
        seen[a[j]] = True

if min_length == float('inf'):
    print(-1)
else:
    print(min_length)