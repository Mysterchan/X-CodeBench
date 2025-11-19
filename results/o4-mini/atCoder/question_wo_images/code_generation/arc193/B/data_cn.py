def count_different_sequences(N, s):
    MOD = 998244353
    
    # Count the number of 1's in the string
    count_ones = s.count('1')
    
    # If there are no 1's, the only sequence is (0, 0, ..., 0)
    if count_ones == 0:
        return 1
    
    # The number of edges from each vertex to the next
    # Each vertex i has edges to (i+1) % N and to N if s[i] == '1'
    # Each vertex i can have 2 choices for the edge to (i+1) % N
    # The total number of sequences is 2^(count_ones) * (count_ones + 1)
    
    # Calculate 2^count_ones % MOD
    power_of_two = pow(2, count_ones, MOD)
    
    # The total number of different sequences
    result = (power_of_two * (count_ones + 1)) % MOD
    
    return result

# Read input
N = int(input().strip())
s = input().strip()

# Output the result
print(count_different_sequences(N, s))