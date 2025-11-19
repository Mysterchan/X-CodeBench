def min_length_B(N, A, Q, queries):
    results = []
    
    def calculate_min_length(A):
        # Count the number of segments of consecutive 1s
        count_segments = 0
        in_segment = False
        
        for value in A:
            if value == 1:
                if not in_segment:
                    count_segments += 1
                    in_segment = True
            else:
                in_segment = False
        
        # The minimum length of B is the number of segments of 1s plus one
        return count_segments + 1 if count_segments > 0 else 0

    # Process each query
    for query in queries:
        index = query - 1  # Convert to 0-based index
        A[index] = 1 - A[index]  # Toggle the value at index
        results.append(calculate_min_length(A))
    
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
results = min_length_B(N, A, Q, queries)

# Print results
for result in results:
    print(result)