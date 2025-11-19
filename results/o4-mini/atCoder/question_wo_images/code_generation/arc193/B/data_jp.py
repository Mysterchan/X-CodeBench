def count_indegree_patterns(N, s):
    MOD = 998244353
    
    # Count the number of 1's in the string
    count_ones = s.count('1')
    
    # If there are no 1's, the only possible indegree pattern is (2, 2, ..., 2)
    if count_ones == 0:
        return 1
    
    # If there are 1's, we can have different indegree patterns
    # The number of ways to choose the indegrees for the vertices 0 to N-1
    # Each vertex can have indegree 0, 1, or 2 from its neighbors
    # Vertex N can have indegree from the vertices with 1's
    
    # The total number of indegree patterns is given by:
    # 2^(count_ones) * 2^(N - count_ones) = 2^N
    # But we need to consider the edges from the 1's to vertex N
    
    # The indegree of vertex N can be from 0 to count_ones
    # Each 1 can either point to N or not, giving us 2^count_ones choices
    # The indegrees of the other vertices can be filled in freely
    
    total_patterns = pow(2, N, MOD)  # 2^N % MOD
    return total_patterns

# Read input
N = int(input().strip())
s = input().strip()

# Get the result
result = count_indegree_patterns(N, s)

# Print the result
print(result)