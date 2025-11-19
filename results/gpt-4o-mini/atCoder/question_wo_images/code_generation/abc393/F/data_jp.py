def longest_increasing_subsequence_up_to(N, Q, A, queries):
    results = []
    for (R, X) in queries:
        # Create a filtered list of available elements
        available = [a for a in A[:R] if a <= X]
        
        # Find the length of the longest strictly increasing subsequence
        if not available:
            results.append(0)
            continue

        from bisect import bisect_left
        lis = []
        for num in available:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = num

        results.append(len(lis))
    
    return results


# Input handling
import sys
input = sys.stdin.read
data = input().splitlines()

first_line = list(map(int, data[0].split()))
N, Q = first_line[0], first_line[1]
A = list(map(int, data[1].split()))
queries = [tuple(map(int, line.split())) for line in data[2:2 + Q]]

# Get results
results = longest_increasing_subsequence_up_to(N, Q, A, queries)

# Print results
for result in results:
    print(result)