def can_form_square(test_cases):
    results = []
    for l1, b1, l2, b2, l3, b3 in test_cases:
        if (l1 == l2 + l3 and b1 == max(b2, b3)) or (b1 == b2 + b3 and l1 == max(l2, l3)):
            results.append("YES")
        else:
            results.append("NO")
    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = can_form_square(test_cases)
print("\n".join(results))