def find_n_m(t, cases):
    results = []
    mod = 10**9 + 7
    
    for a, b, k in cases:
        n = (a - 1) // k + 1
        m = (b - 1) // k + 1
        results.append(f"{n} {m}")
    
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
cases = [tuple(map(int, line.split())) for line in data[1:t + 1]]

# Getting the results
results = find_n_m(t, cases)

# Output results
print("\n".join(results))