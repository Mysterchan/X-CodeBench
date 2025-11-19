def count_snake_numbers(L, R):
    def count_up_to(n):
        if n < 10:
            return 0
        
        s = str(n)
        length = len(s)
        total = 0
        
        # Count all snake numbers with fewer digits
        for d in range(2, length):
            # For d-digit numbers, first digit can be 1-9
            for first in range(1, 10):
                # Remaining d-1 digits must all be < first
                total += first ** (d - 1)
        
        # Count snake numbers with same number of digits as n
        first_digit = int(s[0])
        
        # Count complete groups where first digit is less than n's first digit
        for first in range(1, first_digit):
            total += first ** (length - 1)
        
        # Count numbers with same first digit as n
        # All remaining digits must be < first_digit and <= corresponding digit in n
        def count_with_prefix(pos, tight):
            if pos == length:
                return 1
            
            limit = int(s[pos]) if tight else first_digit - 1
            count = 0
            
            for digit in range(0, min(limit, first_digit) + (1 if tight and int(s[pos]) < first_digit else 0)):
                if digit < first_digit:
                    count += count_with_prefix(pos + 1, tight and digit == int(s[pos]))
            
            return count
        
        # Use dynamic programming for efficiency
        memo = {}
        
        def dp(pos, tight):
            if pos == length:
                return 1
            
            if (pos, tight) in memo:
                return memo[(pos, tight)]
            
            limit = int(s[pos]) if tight else first_digit - 1
            count = 0
            
            for digit in range(0, min(limit + 1, first_digit)):
                new_tight = tight and (digit == int(s[pos]))
                count += dp(pos + 1, new_tight)
            
            memo[(pos, tight)] = count
            return count
        
        total += dp(1, True)
        
        return total
    
    return count_up_to(R) - count_up_to(L - 1)

L, R = map(int, input().split())
print(count_snake_numbers(L, R))