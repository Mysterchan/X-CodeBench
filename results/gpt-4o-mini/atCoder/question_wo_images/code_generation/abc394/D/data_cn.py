def is_colored_bracket_sequence(s):
    stack = []
    matching_bracket = {')': '(', ']': '[', '>': '<'}
    
    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]>':
            if not stack or stack[-1] != matching_bracket[char]:
                return "No"
            stack.pop()

    if not stack:
        return "Yes"
    else:
        return "No"

# Read input
s = input().strip()
# Output result
print(is_colored_bracket_sequence(s))