def lis_length(sequence, limit):
    # Find the length of the longest increasing subsequence with elements at most 'limit'
    from bisect import bisect_left
    
    lis = []  # This will store the end elements of potential increasing subsequences
    for num in sequence:
        if num > limit:
            continue  # skip elements greater than the allowed limit
        pos = bisect_left(lis, num)  # Find index to replace in lis
        if pos == len(lis):
            lis.append(num)  # extend the size of lis
        else:
            lis[pos] = num  # replace the element to maintain the smallest "end" elements
            
    return len(lis)

def process_queries(N, A, queries):
    results = []
    for R, X in queries:
        current_sequence = A[:R]  # Subsequence up to R
        result = lis_length(current_sequence, X)  # Calculate LIS length with limit X
        results.append(result)
    return results

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
A = list(map(int, data[2:N+2]))
queries = []

for i in range(Q):
    R = int(data[N+2 + 2*i])
    X = int(data[N+3 + 2*i])
    queries.append((R, X))

# Process each query and print results
results = process_queries(N, A, queries)
for res in results:
    print(res)