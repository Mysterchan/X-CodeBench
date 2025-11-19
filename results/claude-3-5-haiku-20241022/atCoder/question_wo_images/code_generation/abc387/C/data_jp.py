def count_snake_numbers(L, R):
    def count_up_to(n):
        if n < 10:
            return 0
        
        s = str(n)
        length = len(s)
        total = 0
        
        # Count all snake numbers with fewer digits
        for digits in range(2, length):
            # First digit can be 1-9
            for first in range(1, 10):
                # Remaining digits must all be < first
                total += first ** (digits - 1)
        
        # Count snake numbers with same number of digits but less than n
        first_digit = int(s[0])
        
        # Count numbers with smaller first digit
        for first in range(1, first_digit):
            total += first ** (length - 1)
        
        # Count numbers with same first digit
        # Need to check if we can form valid snake numbers
        max_allowed = first_digit - 1
        
        def count_with_prefix(pos, tight, prefix_str):
            if pos == length:
                # Check if the number we formed is valid
                num_str = prefix_str
                if len(num_str) < 2:
                    return 0
                first = int(num_str[0])
                for i in range(1, len(num_str)):
                    if int(num_str[i]) >= first:
                        return 0
                return 1
            
            if pos == 0:
                # First digit is already set
                return count_with_prefix(1, tight, s[0])
            
            limit = int(s[pos]) if tight else max_allowed
            count = 0
            
            for digit in range(0, min(limit + 1, max_allowed + 1)):
                new_tight = tight and (digit == int(s[pos]))
                count += count_with_prefix(pos + 1, new_tight, prefix_str + str(digit))
            
            return count
        
        total += count_with_prefix(0, True, "")
        
        return total
    
    return count_up_to(R) - count_up_to(L - 1)

L, R = map(int, input().split())
print(count_snake_numbers(L, R))