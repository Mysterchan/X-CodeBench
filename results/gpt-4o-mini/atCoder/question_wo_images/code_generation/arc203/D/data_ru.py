def min_length_b(n, a, q, queries):
    results = []
    
    def calculate_min_length(a):
        # Count the number of segments of consecutive 1s
        count_segments = 0
        in_segment = False
        
        for value in a:
            if value == 1:
                if not in_segment:
                    count_segments += 1
                    in_segment = True
            else:
                in_segment = False
        
        # The minimum length of B is the number of segments of 1s + the number of 0s
        return count_segments + a.count(0)

    for i in range(q):
        idx = queries[i] - 1  # Convert to 0-based index
        a[idx] = 1 - a[idx]  # Toggle the value at index
        
        # Calculate the minimum length of B after the toggle
        min_length = calculate_min_length(a)
        results.append(min_length)
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))
Q = int(data[N+1])
queries = list(map(int, data[N+2:N+2+Q]))

# Get results
results = min_length_b(N, A, Q, queries)

# Print results
for result in results:
    print(result)