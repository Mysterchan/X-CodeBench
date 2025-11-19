def is_balanced(S):
    stack = []
    pairs = {')': '(', ']': '[', '>': '<'}

    for char in S:
        if char in pairs.values():  # If it's an opening bracket
            stack.append(char)
        elif char in pairs.keys():  # If it's a closing bracket
            if stack and stack[-1] == pairs[char]:
                stack.pop()  # Pairs match, pop the last opening bracket
            else:
                return "No"  # Unmatched closing bracket
        
    return "Yes" if not stack else "No"  # Check if any unmatched opening brackets are left

# Input
S = input().strip()

# Output
print(is_balanced(S))