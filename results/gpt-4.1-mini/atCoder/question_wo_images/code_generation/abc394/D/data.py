def is_colorful_bracket_sequence(S: str) -> str:
    stack = []
    pairs = {')': '(', ']': '[', '>': '<'}
    for ch in S:
        if ch in '([{<':
            stack.append(ch)
        else:
            if not stack:
                return "No"
            if stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return "No"
    return "Yes" if not stack else "No"

if __name__ == "__main__":
    S = input().strip()
    print(is_colorful_bracket_sequence(S))