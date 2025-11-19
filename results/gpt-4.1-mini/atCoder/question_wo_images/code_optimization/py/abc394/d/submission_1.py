S = input()

stack = []
pairs = {')': '(', ']': '[', '>': '<'}

for ch in S:
    if ch in '([{<':
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs[ch]:
            print("No")
            break
        stack.pop()
else:
    print("Yes" if not stack else "No")