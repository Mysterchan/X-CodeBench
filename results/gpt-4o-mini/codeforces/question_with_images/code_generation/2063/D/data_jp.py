def max_triangle_score(t, test_cases):
    results = []
    
    for n, m, a, b in test_cases:
        k_max = min(n, m)
        scores = []
        
        if k_max > 0:
            a.sort()
            b.sort()
            for k in range(1, k_max + 1):
                score = 0
                for i in range(k):
                    score += (b[m - 1 - i] - b[i]) * (a[n - 1 - i] - a[i])
                scores.append(score)
        
        results.append((k_max, scores))
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

index = 1
for _ in range(t):
    n, m = map(int, data[index].split())
    a = list(map(int, data[index + 1].split()))
    b = list(map(int, data[index + 2].split()))
    test_cases.append((n, m, a, b))
    index += 3

# Get results
results = max_triangle_score(t, test_cases)

# Output results
output = []
for k_max, scores in results:
    output.append(str(k_max))
    if k_max > 0:
        output.append(" ".join(map(str, scores)))

print("\n".join(output))