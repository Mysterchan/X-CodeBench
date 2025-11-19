def max_increasing_subsequence_length(N, Q, A, queries):
    results = []
    
    for R_i, X_i in queries:
        # Step 1: Filter elements in A[0:R_i] by those <= X_i
        valid_elements = [a for a in A[:R_i] if a <= X_i]
        
        # Step 2: Find the length of the longest increasing subsequence in valid_elements
        if not valid_elements:
            results.append(0)
            continue
        
        lis = []
        
        for num in valid_elements:
            pos = binary_search_insert_position(lis, num)
            if pos < len(lis):
                lis[pos] = num
            else:
                lis.append(num)
        
        results.append(len(lis))
    
    return results

def binary_search_insert_position(lis, num):
    low, high = 0, len(lis)
    while low < high:
        mid = (low + high) // 2
        if lis[mid] < num:
            low = mid + 1
        else:
            high = mid
    return low

# Input read
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])
A = list(map(int, data[2:N + 2]))
queries = []
for i in range(Q):
    R_i = int(data[N + 2 + 2 * i])
    X_i = int(data[N + 2 + 2 * i + 1])
    queries.append((R_i, X_i))

# Compute results
results = max_increasing_subsequence_length(N, Q, A, queries)

# Output results
for result in results:
    print(result)