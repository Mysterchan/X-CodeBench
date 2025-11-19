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
                # Remaining digits must be < first
                total += first ** (digits - 1)
        
        # Count snake numbers with same number of digits but less than n
        for i in range(length):
            first_digit = int(s[0])
            current_digit = int(s[i])
            
            if i == 0:
                # Count numbers starting with digits less than first_digit
                for d in range(1, first_digit):
                    total += d ** (length - 1)
            else:
                # Count numbers with same prefix but smaller digit at position i
                for d in range(0, current_digit):
                    if d < first_digit:
                        total += first_digit ** (length - 1 - i)
                
                # Check if current digit violates snake property
                if current_digit >= first_digit:
                    break
        else:
            # n itself is a snake number
            total += 1
        
        return total
    
    return count_up_to(R) - count_up_to(L - 1)

L, R = map(int, input().split())
print(count_snake_numbers(L, R))