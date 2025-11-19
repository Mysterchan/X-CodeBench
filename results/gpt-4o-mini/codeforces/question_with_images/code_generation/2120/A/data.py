def can_form_square(test_cases):
    results = []
    for l1, b1, l2, b2, l3, b3 in test_cases:
        # Attempting to check possible arrangements to form a square
        # Check if we can stack them to form a square
        if (l1 == l2 and b1 == b2 + b3) or (l1 == l2 and b2 == b1 + b3) or (l1 == l2 + l3 and b1 == b2) or (l1 == l2 and b3 == b1 + b2):
            results.append("YES")
        # Check if the largest rectangle can accommodate the combined area of the other two
        elif (l1 == l2 + l3 and b1 == max(b2, b3)) or (l1 == max(l2, l3) and b1 == b2 + b3):
            results.append("YES")
        # We can also check for a setting where:
        elif (b1 == b2 and l1 == l2 + l3) or (b1 == b2 and l2 == l1 + l3) or (b1 == max(b2, b3) and l1 == l2 + l3):
            results.append("YES")
        else:
            results.append("NO")
    return results

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    test_cases.append(tuple(map(int, input().split())))

results = can_form_square(test_cases)
# Print results
for result in results:
    print(result)