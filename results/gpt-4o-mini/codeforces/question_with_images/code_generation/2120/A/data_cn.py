def can_form_square(l1, b1, l2, b2, l3, b3):
    # Check if they can fit into a square
    max_side = max(l1, b1)
    total_height = b1 + b2 + b3
    return total_height == max_side

t = int(input())
results = []
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    if can_form_square(l1, b1, l2, b2, l3, b3):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))