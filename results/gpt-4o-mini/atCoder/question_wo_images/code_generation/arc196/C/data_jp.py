def count_strongly_connected_pairs(N, S):
    MOD = 998244353
    
    # Count the number of W's and B's
    count_W = S.count('W')
    count_B = S.count('B')
    
    # If the counts of W and B are not equal, return 0
    if count_W != N or count_B != N:
        return 0
    
    # Initialize the number of valid pairings
    valid_pairings = 1
    
    # We will use a stack to track the balance of W's and B's
    balance = 0
    for char in S:
        if char == 'W':
            balance += 1
        else:  # char == 'B'
            balance -= 1
        
        # If at any point balance goes negative, it's impossible to form a valid pairing
        if balance < 0:
            return 0
        
        # The number of valid pairings is multiplied by the number of ways to choose
        # a W for each B encountered so far
        valid_pairings *= balance
        valid_pairings %= MOD
    
    return valid_pairings

# Read input
N = int(input().strip())
S = input().strip()

# Output the result
print(count_strongly_connected_pairs(N, S))