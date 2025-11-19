def mod_inv(a, p):
    # Function to compute modular inverse using Extended Euclidean Algorithm
    return pow(a, p - 2, p)

def preprocess_factorials_and_inverses(max_n, mod):
    # Precompute factorials and their modular inverses
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
        
    inv_fact[max_n] = mod_inv(fact[max_n], mod)
    
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
        
    return fact, inv_fact

def count_permutations(n, m, parent, colors, destinations, mod):
    # Create color counts for black and white chips
    color_count = [0, 0]
    
    for color in colors:
        color_count[color] += 1
    
    # Count how many chips can go to each depth
    depth_count = [0] * (n + 1)
    
    for d in destinations:
        depth_count[d] += 1
        
    # Create a dp array to manage the counts of configurations
    dp = [0] * (m + 1)
    dp[0] = 1
    
    for depth in range(n + 1):
        if depth_count[depth] > 0:
            total_chips_at_depth = depth_count[depth]
            new_dp = [0] * (m + 1)
            for i in range(m + 1):
                if dp[i] != 0:
                    for j in range(total_chips_at_depth + 1):
                        if i + j <= m:
                            new_dp[i + j] = (new_dp[i + j] + dp[i] * fact[total_chips_at_depth] * inv_fact[j] * inv_fact[total_chips_at_depth - j]) % mod
            dp = new_dp
            
    return dp[m]

mod = 998244353
fact, inv_fact = preprocess_factorials_and_inverses(5000, mod)

t = int(input())
results = []
for _ in range(t):
    n, m = map(int, input().split())
    parent = list(map(int, input().split()))
    colors = list(map(int, input().split()))
    destinations = list(map(int, input().split()))
    
    result = count_permutations(n, m, parent, colors, destinations, mod)
    results.append(result)

# Print all results for each test case
for res in results:
    print(res)