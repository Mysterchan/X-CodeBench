def count_distinct_sequences(N, s):
    MOD = 998244353
    
    # Count the number of 1's in the string
    count_ones = s.count('1')
    
    # If there are no 1's, the only possible in-degrees are (0, 0, ..., 0)
    if count_ones == 0:
        return 1
    
    # The number of distinct sequences is given by the formula:
    # (count_ones + 1) ** (N - count_ones) % MOD
    # This is because for each of the (N - count_ones) vertices that are connected to the last vertex,
    # we can choose to direct the edges to any of the (count_ones + 1) vertices (including the last vertex).
    
    result = pow(count_ones + 1, N - count_ones, MOD)
    
    return result

# Read input
N = int(input().strip())
s = input().strip()

# Get the result and print it
print(count_distinct_sequences(N, s))