def main():
    S = input().strip()
    stack = []
    pairs = {')': '(', ']': '[', '>': '<'}

    for ch in S:
        if ch in '([{<':
            stack.append(ch)
        else:
            if not stack:
                print("No")
                return
            if stack[-1] == pairs[ch]:
                stack.pop()
            else:
                print("No")
                return

    print("Yes" if not stack else "No")

if __name__ == "__main__":
    main()