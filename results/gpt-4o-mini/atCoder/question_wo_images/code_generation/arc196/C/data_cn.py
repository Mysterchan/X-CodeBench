def count_ways_to_pair(N, S):
    MOD = 998244353
    
    # Count the number of W's and B's
    count_W = S.count('W')
    count_B = S.count('B')
    
    # If the counts of W and B are not equal, return 0
    if count_W != count_B:
        return 0
    
    # Initialize the balance and the number of valid configurations
    balance = 0
    valid_pairs = 1
    
    for char in S:
        if char == 'W':
            balance += 1
        else:  # char == 'B'
            balance -= 1
        
        # If at any point balance is negative, it's invalid
        if balance < 0:
            return 0
        
        # The number of valid configurations is the number of ways to choose pairs
        # This is calculated using the formula for Catalan numbers
        # C(n) = (2n)! / ((n + 1)! * n!)
        # We can use the fact that C(n) = C(n-1) * (2*(2*n-1)) / (n+1)
        if balance == 0:
            valid_pairs = (valid_pairs * (2 * count_W - 1)) % MOD
            count_W -= 1
    
    return valid_pairs

# Read input
N = int(input().strip())
S = input().strip()

# Calculate and print the result
print(count_ways_to_pair(N, S))