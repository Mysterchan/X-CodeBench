def is_colorful_bracket_sequence(S):
    stack = []
    matching_brackets = {')': '(', ']': '[', '>': '<'}

    for char in S:
        if char in matching_brackets.values():  # If it's an opening bracket
            stack.append(char)
        elif char in matching_brackets.keys():  # If it's a closing bracket
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()  # Valid match found, pop the last opening bracket
            else:
                print("No")
                return

    if not stack:  # If stack is empty, all brackets matched
        print("Yes")
    else:
        print("No")

S = input()
is_colorful_bracket_sequence(S)