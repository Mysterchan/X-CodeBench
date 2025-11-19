def is_colorful_bracket_sequence(S):
    stack = []
    matching_brackets = {')': '(', ']': '[', '>': '<'}

    for char in S:
        if char in '([{':
            stack.append(char)
        elif char in ')]}>':
            if not stack or stack[-1] != matching_brackets[char]:
                print("No")
                return
            stack.pop()

    if not stack:
        print("Yes")
    else:
        print("No")

# Read input
S = input().strip()
is_colorful_bracket_sequence(S)