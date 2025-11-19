def is_colored_bracket_sequence(S):
    stack = []
    matching_bracket = {')': '(', ']': '[', '>': '<'}
    
    for char in S:
        if char in '([{':
            stack.append(char)
        elif char in ')]}>':
            if not stack or stack[-1] != matching_bracket[char]:
                return "No"
            stack.pop()
    
    return "Yes" if not stack else "No"

# Read input
S = input().strip()
# Print output
print(is_colored_bracket_sequence(S))