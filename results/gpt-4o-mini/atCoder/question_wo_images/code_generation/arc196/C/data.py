def count_strongly_connected_partitions(N, S):
    MOD = 998244353
    
    # Count the number of white and black vertices
    white_count = S.count('W')
    black_count = S.count('B')
    
    # If the counts of white and black are not equal, return 0
    if white_count != black_count:
        return 0
    
    # Initialize the factorial and inverse factorial arrays
    fact = [1] * (N + 1)
    inv_fact = [1] * (N + 1)
    
    # Precompute factorials and inverse factorials
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)  # Fermat's little theorem for inverse
    for i in range(N - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
    
    # Count the number of valid partitions
    balance = 0
    valid_partitions = 0
    
    for char in S:
        if char == 'W':
            balance += 1
        else:
            balance -= 1
        
        # If at any point balance is negative, we cannot have a valid partition
        if balance < 0:
            return 0
        
        # Count valid partitions when balance is zero
        if balance == 0:
            valid_partitions += 1
    
    # If we have an odd number of valid partitions, return 0
    if valid_partitions % 2 != 0:
        return 0
    
    # The number of ways to pair them is (N!)^2
    result = fact[N] * fact[N] % MOD
    return result

# Read input
N = int(input().strip())
S = input().strip()

# Calculate and print the result
print(count_strongly_connected_partitions(N, S))