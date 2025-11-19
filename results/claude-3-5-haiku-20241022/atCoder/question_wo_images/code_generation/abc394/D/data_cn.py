def is_colorful_bracket_sequence(s):
    stack = []
    pairs = {'(': ')', '[': ']', '<': '>'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack:
                return False
            if pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

s = input().strip()
if is_colorful_bracket_sequence(s):
    print("Yes")
else:
    print("No")