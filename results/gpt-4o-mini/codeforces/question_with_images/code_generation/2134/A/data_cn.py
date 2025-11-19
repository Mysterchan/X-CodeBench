def can_be_symmetric(n, a, b):
    # The length of the cells is n, a is the range for red, and b is the range for blue.
    # If we can place the segments to make sure they are symmetric, we can have:
    # The two segments starting points must not overlap incorrectly.
    
    # We will only check non-overlapping conditions based on symmetry
    if (n - a) >= b or (n - b) >= a:
        return "YES"
    
    return "NO"

t = int(input())
results = []

for _ in range(t):
    n, a, b = map(int, input().split())
    results.append(can_be_symmetric(n, a, b))

print("\n".join(results))