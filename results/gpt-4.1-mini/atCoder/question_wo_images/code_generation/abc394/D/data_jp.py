def main():
    S = input()
    stack = []
    pairs = {')': '(', ']': '[', '>': '<'}

    for c in S:
        if c in '([{<':
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                print("No")
                return
            stack.pop()
    print("Yes" if not stack else "No")

if __name__ == "__main__":
    main()