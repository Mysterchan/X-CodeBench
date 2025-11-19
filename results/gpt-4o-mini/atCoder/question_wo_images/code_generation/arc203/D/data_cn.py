def min_length_after_queries(N, A, Q, queries):
    results = []
    
    def calculate_min_length():
        # Count the number of segments of consecutive 1s
        count = 0
        in_segment = False
        for value in A:
            if value == 1:
                if not in_segment:
                    count += 1
                    in_segment = True
            else:
                in_segment = False
        return count + (1 if count > 0 else 0)  # Add 1 if there are segments of 1s

    for query in queries:
        index = query - 1  # Convert to 0-based index
        A[index] ^= 1  # Toggle the value at the index
        results.append(calculate_min_length())
    
    return results

# Read input
N = int(input().strip())
A = list(map(int, input().strip().split()))
Q = int(input().strip())
queries = [int(input().strip()) for _ in range(Q)]

# Get results
results = min_length_after_queries(N, A, Q, queries)

# Print results
for result in results:
    print(result)