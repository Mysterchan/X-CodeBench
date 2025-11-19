def compute_sum_of_permutations(N):
    MOD = 998244353
    
    # This will hold the final sum
    sum_f = 0
    
    # Initialize a value that represents 10^k where k is the number of digits
    power_of_ten = 1
    
    # Factorial to count permutations
    factorial = 1
    
    # We loop through each position from 0 to N-1
    for i in range(N):
        # Current digit contributes to f(P) as the first part in N! permutations
        # Each number k contributes 1 time at the leading place in N!/N = (N-1)!
        contrib_factor = (factorial * (N - i)) % MOD
        
        # Calculate the value t for digit position i (1 to N, hence i + 1)
        t = (i + 1) * contrib_factor % MOD
        
        # Update the sum with the current contribution times the current power of ten
        sum_f = (sum_f + t * power_of_ten) % MOD
        
        # Update the power_of_ten for the next digit position
        power_of_ten = (power_of_ten * 10) % MOD
        
        # Update factorial (to account for total permutations)
        factorial = factorial * (i + 1) % MOD
    
    return sum_f

# Main execution
N = int(input().strip())
result = compute_sum_of_permutations(N)
print(result)