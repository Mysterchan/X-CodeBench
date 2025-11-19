def min_length_b(n, a, queries):
    results = []
    count_segments = 0
    last_value = -1

    for value in a:
        if value != last_value:
            count_segments += 1
            last_value = value

    for query in queries:
        index = query - 1
        a[index] ^= 1  # Toggle the value at index

        # Recalculate the number of segments
        count_segments = 0
        last_value = -1

        for value in a:
            if value != last_value:
                count_segments += 1
                last_value = value

        results.append(count_segments)

    return results

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))
Q = int(data[N+1])
queries = list(map(int, data[N+2:N+2+Q]))

# Get results
results = min_length_b(N, A, queries)

# Output results
for result in results:
    print(result)