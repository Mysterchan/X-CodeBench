def count_snake_numbers(limit):
    s = str(limit)
    n = len(s)
    
    # Count snake numbers from 10 to limit
    total = 0
    
    # For each length from 2 to n-1 (complete lengths less than n)
    for length in range(2, n):
        # For each possible first digit d (1-9)
        for d in range(1, 10):
            # Remaining length-1 digits must be < d
            # So we have d choices for each position
            total += d ** (length - 1)
    
    # For length n (same as limit), we need to be more careful
    # Use digit DP approach
    def count_with_prefix(pos, first_digit, tight):
        if pos == n:
            return 1
        
        if pos == 0:
            # Choose first digit
            result = 0
            max_digit = int(s[0]) if tight else 9
            for d in range(1, max_digit + 1):
                new_tight = tight and (d == int(s[0]))
                result += count_with_prefix(pos + 1, d, new_tight)
            return result
        else:
            # Choose subsequent digits (must be < first_digit)
            result = 0
            max_digit = int(s[pos]) if tight else 9
            upper = min(max_digit, first_digit - 1)
            
            for d in range(0, upper + 1):
                new_tight = tight and (d == int(s[pos]))
                result += count_with_prefix(pos + 1, first_digit, new_tight)
            return result
    
    total += count_with_prefix(0, -1, True)
    
    return total

def solve(L, R):
    # Count snake numbers in [L, R]
    # = count(R) - count(L-1)
    
    count_R = count_snake_numbers(R)
    count_L_minus_1 = count_snake_numbers(L - 1) if L > 10 else 0
    
    return count_R - count_L_minus_1

# Read input
L, R = map(int, input().split())
print(solve(L, R))