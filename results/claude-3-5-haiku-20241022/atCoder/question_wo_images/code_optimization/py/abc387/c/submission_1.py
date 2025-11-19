def count_snake(n):
    if n < 10:
        return 0
    
    s = str(n)
    length = len(s)
    total = 0
    
    # Count snake numbers with fewer digits than n
    for num_digits in range(2, length):
        # First digit can be 1-9
        for first_digit in range(1, 10):
            # Remaining digits must be < first_digit
            total += first_digit ** (num_digits - 1)
    
    # Count snake numbers with same number of digits as n
    for first_digit in range(1, int(s[0]) + 1):
        if first_digit < int(s[0]):
            # Any combination works for remaining digits < first_digit
            total += first_digit ** (length - 1)
        else:
            # first_digit == int(s[0]), need to count more carefully
            # Use recursion/iteration to count valid suffixes
            count = 0
            max_allowed = first_digit - 1
            
            # Build suffix respecting the bound from n
            def count_suffix(pos, tight):
                if pos == length:
                    return 1
                
                nonlocal count
                limit = int(s[pos]) if tight else 9
                
                for digit in range(0, min(limit, max_allowed) + 1):
                    if digit > max_allowed:
                        break
                    if tight and digit == limit:
                        count_suffix(pos + 1, True)
                    else:
                        # Not tight anymore, all remaining can be 0 to max_allowed
                        remaining = length - pos - 1
                        count += (max_allowed + 1) ** remaining
                        break
                        
            count_suffix(1, True)
            total += count
    
    return total

L, R = map(int, input().split())
print(count_snake(R) - count_snake(L - 1))