def total_matches(n):
    return n - 1 + (n // 2)

t = int(input())
for _ in range(t):
    n = int(input())
    print(total_matches(n))