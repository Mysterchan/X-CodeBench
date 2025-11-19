n, m = map(int, input().split())
for _ in range(m):
    input()

total_edges = n * (n - 1) // 2

if m % 2 == total_edges % 2:
    print(total_edges)
else:
    print(total_edges - 1)