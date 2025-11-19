import sys

def is_colorful_bracket_sequence(s: str) -> bool:
    # Mapping from closing bracket to its corresponding opening bracket
    matching = {')': '(', ']': '[', '>': '<'}
    stack = []
    for ch in s:
        if ch in '([<':
            stack.append(ch)
        else:  # ch in ')]>'
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    return not stack

def main():
    s = sys.stdin.readline().strip()
    print("Yes" if is_colorful_bracket_sequence(s) else "No")

if __name__ == "__main__":
    main()