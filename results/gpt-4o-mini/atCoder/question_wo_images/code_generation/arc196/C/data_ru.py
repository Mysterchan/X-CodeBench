def count_strongly_connected_pairs(N, S):
    MOD = 998244353
    
    # Count the number of W's and B's
    count_W = S.count('W')
    count_B = S.count('B')
    
    # If the counts of W and B are not equal, return 0
    if count_W != count_B:
        return 0
    
    # Initialize the balance and the number of valid configurations
    balance = 0
    valid_configurations = 1
    
    # Iterate through the string to calculate balance
    for char in S:
        if char == 'W':
            balance += 1
        else:
            balance -= 1
        
        # If at any point balance goes negative, it's invalid
        if balance < 0:
            return 0
        
        # The number of valid configurations is multiplied by the current balance
        valid_configurations = (valid_configurations * balance) % MOD
    
    return valid_configurations

# Read input
N = int(input().strip())
S = input().strip()

# Output the result
print(count_strongly_connected_pairs(N, S))