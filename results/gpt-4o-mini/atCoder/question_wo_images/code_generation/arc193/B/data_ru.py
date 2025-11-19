def count_sequences(N, s):
    MOD = 998244353
    
    # Count the number of 1's in the string
    count_ones = s.count('1')
    
    # If there are no 1's, the only sequence is (0, 0, ..., 0)
    if count_ones == 0:
        return 1
    
    # If there are 1's, we can calculate the number of sequences
    # The number of ways to direct edges from the 1's to the other nodes
    # Each 1 can connect to any of the N nodes (including itself)
    # Each edge can be directed in 2 ways (u -> v or v -> u)
    
    # The number of edges from 1's to N is count_ones
    # The number of edges in the cycle is N (from i to (i+1) % N)
    
    # Total edges = count_ones + N
    total_edges = count_ones + N
    
    # Each edge can be directed in 2 ways
    result = pow(2, total_edges, MOD)
    
    return result

# Read input
N = int(input().strip())
s = input().strip()

# Get the result and print it
print(count_sequences(N, s))