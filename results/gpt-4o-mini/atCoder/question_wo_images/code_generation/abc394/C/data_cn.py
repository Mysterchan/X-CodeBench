def replace_wa_with_ac(s):
    s = list(s)  # Convert string to a list for mutability
    i = 0
    while i < len(s) - 1:
        if s[i] == 'W' and s[i + 1] == 'A':
            s[i] = 'A'
            s[i + 1] = 'C'
            i += 2  # Move past the replaced substring
        else:
            i += 1  # Move to the next character
    return ''.join(s)  # Convert list back to string

# Read input
s = input().strip()
# Get result
result = replace_wa_with_ac(s)
# Output result
print(result)