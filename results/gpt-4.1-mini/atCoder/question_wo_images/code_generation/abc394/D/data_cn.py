def main():
    S = input().strip()
    stack = []
    pairs = {')': '(', ']': '[', '>': '<'}
    for ch in S:
        if ch in '([{<':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                print("No")
                return
            stack.pop()
    print("Yes" if not stack else "No")

if __name__ == "__main__":
    main()