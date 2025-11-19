t = int(input())
results = []

for _ in range(t):
    n, a, b = map(int, input().split())
    # Check if a and b can be placed symmetrically
    if (n - a >= b - 1) or (n - b >= a - 1):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))