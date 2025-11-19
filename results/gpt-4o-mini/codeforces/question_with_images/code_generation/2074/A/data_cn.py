def can_form_square(l, r, d, u):
    # Check if the points can form a square
    return (l == r) and (d == u)

t = int(input())
results = []
for _ in range(t):
    l, r, d, u = map(int, input().split())
    if can_form_square(l, r, d, u):
        results.append("Yes")
    else:
        results.append("No")

print("\n".join(results))