def max_triangle_score(test_cases):
    results = []
    
    for n, a in test_cases:
        max_score = 0
        
        # Iterate through all combinations of three different vertices
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Calculate the score for the triangle formed by vertices i, j, k
                    score = a[i] * a[j] * a[k]
                    max_score = max(max_score, score)
        
        results.append(max_score)
    
    return results

# Read input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Get results
results = max_triangle_score(test_cases)

# Print results
for result in results:
    print(result)