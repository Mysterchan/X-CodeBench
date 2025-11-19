MOD = 998244353

def solve():
    N = int(input())
    
    # Precompute factorials
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i-1] * i % MOD
    
    # For each number i from 1 to N, calculate its contribution
    total = 0
    
    for i in range(1, N + 1):
        # Get the string representation and its length
        s = str(i)
        d = len(s)
        
        # For each position where number i can appear in the permutation
        for pos in range(N):
            # Count of numbers after position pos
            after = N - pos - 1
            
            # Number of permutations where i is at position pos
            count = fact[N - 1]
            
            # Calculate the positional value
            # The number i contributes s * 10^(sum of digits of numbers after it)
            # We need to sum over all possible sets of numbers that come after i
            
            # Expected number of digits after position pos
            # For each of the (N-1) other numbers, it appears after i in (N-1)!/(N) * N = (N-1)!/1 arrangements
            # But we need to be more careful
            
            # For a fixed position pos, and number i at that position:
            # - There are (pos)! ways to arrange numbers before i
            # - There are (after)! ways to arrange numbers after i
            # Total: pos! * after!
            
            ways_at_pos = fact[pos] * fact[after] % MOD
            
            # Now calculate contribution of i at position pos
            # It contributes: value_of_i * 10^(total_digits_after)
            
            # Sum of digits after position pos over all valid permutations
            total_digits_after = 0
            for j in range(1, N + 1):
                if j == i:
                    continue
                # Number j appears after position pos in some permutations
                # When i is at pos, j can be at any of the 'after' positions
                # Probability j is after i: after / (N-1)
                # Number of arrangements: ways_at_pos * after / (N-1)
                if after > 0:
                    times_j_after = ways_at_pos * after * pow(N - 1, MOD - 2, MOD) % MOD
                    total_digits_after = (total_digits_after + len(str(j)) * times_j_after) % MOD
            
            # Contribution of i at position pos
            value = int(s)
            # power of 10
            power10 = pow(10, total_digits_after, MOD)
            contribution = value * power10 % MOD
            total = (total + contribution) % MOD
    
    print(total)

solve()