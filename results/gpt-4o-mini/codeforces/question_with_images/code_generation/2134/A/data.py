# Read number of test cases
t = int(input())
results = []

for _ in range(t):
    n, a, b = map(int, input().split())
    
    # Calculate maximum possible painted length
    if (n - a + 1) + (n - b + 1) >= n:
        results.append("YES")
    else:
        results.append("NO")

# Print all results
print("\n".join(results))