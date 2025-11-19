def calculate_sum_of_permutation_values(N):
    MOD = 998244353
    # base factors for positions
    total_sum = 0
    # factorial and position multiplier
    pos_multiplier = 1  # for the place value (1, 10, 100,...)
    
    # total permutations = N!
    # calculate factorial(N)
    factorial = 1
    for i in range(2, N + 1):
        factorial = (factorial * i) % MOD
        
    for position in range(1, N + 1):
        # For each number in position `position`, it can contribute to (N-1)! permutations
        # The weight of the position in decimal system is `pos_multiplier`
        total_sum = (total_sum + (pos_multiplier * factorial) % MOD) % MOD
        # Update the position multiplier (like 1, 10, 100, ...)
        pos_multiplier = (pos_multiplier * 10) % MOD
        
    # Since we counted each place weight for each element's contributions,
    # we multiply by N! since each can appear in N! permutations
    total_sum = (total_sum * factorial) % MOD
    
    return total_sum

N = int(input())
result = calculate_sum_of_permutation_values(N)
print(result)