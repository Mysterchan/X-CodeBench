MOD = 998244353

def solve(N):
    # Precompute number of digits for each number
    digits = [0] * (N + 1)
    for i in range(1, N + 1):
        digits[i] = len(str(i))
    
    total_digits = sum(digits[1:])
    factorial = [1] * (N + 1)
    for i in range(1, N + 1):
        factorial[i] = factorial[i-1] * i % MOD
    
    result = 0
    
    # For each position j (0-indexed: 0 to N-1)
    for j in range(N):
        # For each number i at position j
        for i in range(1, N + 1):
            # Digits after position j (from the remaining N-1-j numbers)
            remaining_count = N - 1 - j
            total_digits_without_i = total_digits - digits[i]
            
            # Sum of 10^(digit_sum) over all subsets of size remaining_count
            # from {1,...,N}\{i}
            if remaining_count == 0:
                contribution = i * factorial[N-1] % MOD
            else:
                # For all subsets of remaining numbers of size remaining_count
                # Average digit sum = remaining_count * total_digits_without_i / (N-1)
                # Sum over all subsets = C(N-1, remaining_count) * sum of 10^(digit_sums)
                
                # Use DP or direct computation
                power_sum = 0
                # This is complex, let me use a different approach
                
                # Contribution when digits after = d: i * 10^d * (# of such arrangements)
                # Need to count subsets with specific digit sums
                pass
    
    return result

N = int(input())
print(solve(N))