def is_symmetric_possible(n, a, b):
    # Checking the condition for symmetry
    return (a + b - 1) <= n and (n - a) % 2 == (n - b) % 2

t = int(input())
results = []
for _ in range(t):
    n, a, b = map(int, input().split())
    results.append("YES" if is_symmetric_possible(n, a, b) else "NO")

print("\n".join(results))